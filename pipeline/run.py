import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

import logging

from config.beam_config import BeamConfig, SetupBeamEnv


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger()

pipeline_options = PipelineOptions.from_dictionary(BeamConfig(SetupBeamEnv.PROD).get_pipeline_options())

with beam.Pipeline(options=pipeline_options) as p:
    (p
     | 'ReadFromPubSub' >> beam.io.ReadFromPubSub(subscription='projects/ivanildobarauna/subscriptions/gcp-streaming-pipeline-pull')
     | 'Window' >> beam.WindowInto(beam.window.FixedWindows(1))
     | 'WriteToGCS' >> beam.io.WriteToText(
                'gs://gcp-streaming-pipeline-dataflow/output/test.txt',
                file_name_suffix='.txt', num_shards=1
            )
     )

