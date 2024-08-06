from src.api.application.ports.send_metrics import ISendMetrics


class SendMetricsService:
    def __init__(self, send_metrics_repository: ISendMetrics) -> None:
        self.send_metrics_repository = send_metrics_repository

    def send(self, metric_name: str, metric_value: int) -> None:
        self.send_metrics_repository.send_metric(metric_name, metric_value)
