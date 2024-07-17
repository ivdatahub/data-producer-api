from datetime import datetime
from enum import Enum
def default_timestamp_str() -> str: return str(int(datetime.now().timestamp()))


class EnvSetup(Enum):
    PROD = 0,
    TEST = 1
