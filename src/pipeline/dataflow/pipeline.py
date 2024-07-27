import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

from src.pipeline.config.common import default_timestamp_formated
from src.pipeline.config.beam_config import BeamConfig
from src.pipeline.config.common import EnvSetup, Constants


def set_key(element):
    key = eval(element)["created_at"]
    return str(key)[:8], element


def print_count(element):
    print(f"{default_timestamp_formated()} Qtde Messages Processed: {len(element[0][1])}")


pipeline_options = PipelineOptions.from_dictionary(BeamConfig(EnvSetup.PROD).get_pipeline_options())

with beam.Pipeline(options=pipeline_options) as p:
    messages = p | 'ReadFromPubSub' >> beam.io.ReadFromPubSub(subscription=Constants.PUBSUB_SUBSCRIPTION)
    decoded_messages = messages | 'Decode' >> beam.Map(lambda x: x.decode('utf-8'))
    keyed_messages = decoded_messages | 'CreateKey' >> beam.Map(set_key)
    windowed_messages = keyed_messages | 'Window' >> beam.WindowInto(beam.window.FixedWindows(60))
    grouped_messages = windowed_messages | 'GroupbyMessage' >> beam.GroupByKey()
    counted_messages = grouped_messages | 'CountPerWindow' >> beam.combiners.Count.PerElement()
    counted_messages | 'Print' >> beam.Map(print_count)
