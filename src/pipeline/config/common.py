from datetime import datetime
from enum import Enum
import logging


class Constants:
    GCP_PROJECT = "ivanildobarauna"
    PUBSUB_SUBSCRIPTION = f"projects/{GCP_PROJECT}/subscriptions/gcp-streaming-pipeline-pull"


def default_timestamp_str() -> str: return str(int(datetime.now().timestamp()))


def default_timestamp_formated() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class EnvSetup(Enum):
    PROD = 0,
    TEST = 1


def logger():
    logging.basicConfig(
        level=logging.CRITICAL,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    return logging.getLogger()
