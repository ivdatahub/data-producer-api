import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

from src.pipeline.config.common import logger, default_timestamp_formated
from src.pipeline.config.beam_config import BeamConfig
from src.pipeline.config.common import EnvSetup
from datetime import datetime

pipeline_logger = logger()

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