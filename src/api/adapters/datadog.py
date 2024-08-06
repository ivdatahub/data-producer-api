from src.api.application.ports.send_metrics import ISendMetrics
from src.api.application.use_cases.get_metrics_server import get_metrics_server_address
from datadog import initialize, statsd


class DataDogAdapter(ISendMetrics):
    def __init__(self) -> None:
        self.client_options = {
            "statsd_host": get_metrics_server_address(),
            "statsd_port": 8125,
        }
        self.dd_client = initialize(**self.client_options)

    def send_metric(self, metric_name: str, metric_value: int) -> None:
        statsd.increment(metric=metric_name, value=metric_value)
