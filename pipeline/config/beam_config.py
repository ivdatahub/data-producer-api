from enum import Enum
from datetime import datetime


class SetupBeamEnv(Enum):
    PROD = 0,
    TEST = 1


def default_timestamp_str() -> str: return str(int(datetime.now().timestamp()))


class BeamConfig:
    def __init__(self, env: SetupBeamEnv):
        self.env = env

    def get_pipeline_options(self) -> dict:
        if self.env == SetupBeamEnv.PROD:
            return {
                'runner': 'DataflowRunner',
                'project': 'ivanildobarauna',
                'region': 'us-central1',
                'temp_location': ' gs://gcp-streaming-pipeline-dataflow/temp',
                'staging_location': 'gs://gcp-streaming-pipeline-dataflow/staging',
                'min_workers': 1,
                'num_workers': 1,
                'max_num_workers': 2,
                'autoscaling_algorithm': 'THROUGHPUT_BASED',
                'save_main_session': True,
                'machine_type': 'n1-standard-1',
                'job_name': f'gcp-streaming-pipeline{default_timestamp_str()}',
                'disk_size_gb': '10',
                'streaming': True
            }
        else:
            return {
                'runner': 'DirectRunner',
                'save_main_session': True,
                'num_workers': 1,
                'job_name': f'hello-world-job{default_timestamp_str()}',
                'disk_size_gb': '10',
                'streaming': True
            }

