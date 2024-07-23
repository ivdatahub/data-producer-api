<<<<<<< HEAD
from datetime import datetime

=======
>>>>>>> c1f3495 (feature: Dataflow changes development)
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

from src.pipeline.config.common import logger, default_timestamp_formated
from src.pipeline.config.beam_config import BeamConfig
<<<<<<< HEAD
from src.pipeline.config.common import EnvSetup, Constants

=======
from src.pipeline.config.common import EnvSetup
from datetime import datetime

pipeline_logger = logger()
>>>>>>> c1f3495 (feature: Dataflow changes development)

def set_key(element):
    key = eval(element)["created_at"]
    return str(key)[:8], element


def print_count(element):
    print(f"{default_timestamp_formated()} Qtde Messages Processed: {len(element[0][1])}")


# pipeline_logger = logger()
pipeline_options = PipelineOptions.from_dictionary(BeamConfig(EnvSetup.TEST).get_pipeline_options())


def set_key(element):
    return "test", element

def count_messages(element):
    return len(element[1])


def add_timestamp(element):
    dic = eval(element)
    dic["processed_at"] = default_timestamp_formated()
    return str(dic)


def timestamp_to_datetime(element):
    dic = eval(element)
    dic["created_at"] = str(datetime.fromtimestamp(dic["created_at"]))
    return str(dic)


with beam.Pipeline(options=pipeline_options) as p:
<<<<<<< HEAD
    messages = p | 'ReadFromPubSub' >> beam.io.ReadFromPubSub(subscription=Constants.PUBSUB_SUBSCRIPTION)
    decoded_messages = messages | 'Decode' >> beam.Map(lambda x: x.decode('utf-8'))
    keyed_messages = decoded_messages | 'CreateKey' >> beam.Map(set_key)
    windowed_messages = keyed_messages | 'Window' >> beam.WindowInto(beam.window.FixedWindows(60))
    grouped_messages = windowed_messages | 'GroupbyMessage' >> beam.GroupByKey()
    counted_messages = grouped_messages | 'CountPerWindow' >> beam.combiners.Count.PerElement()
    counted_messages | 'Print' >> beam.Map(print_count)
=======
    (p
     | 'ReadFromPubSub' >> beam.io.ReadFromPubSub(subscription='projects/ivanildobarauna/subscriptions/gcp-streaming-pipeline-pull')
     | 'Decode' >> beam.Map(lambda x: x.decode('utf-8'))
     | 'AddTimestamp' >> beam.Map(add_timestamp)
     | 'TransformTimestamp' >> beam.Map(timestamp_to_datetime)
     | 'CreateKey' >> beam.Map(set_key)
     | 'Window' >> beam.WindowInto(beam.window.FixedWindows(5))
     | 'GroupbyMessage' >> beam.GroupByKey()
     # | 'CountMessage' >> beam.Map(count_messages)
     | 'Print' >> beam.Map(print)

     # | 'PrintKey' >> beam.Map(print)
     # | 'PrintMessage' >> beam.Map(print)
     )
>>>>>>> c1f3495 (feature: Dataflow changes development)
