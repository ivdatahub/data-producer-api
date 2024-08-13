from src.api.application.ports.send_metrics import ISendMetrics


class SendMetricsService:
    def __init__(self, send_metrics_repository: ISendMetrics) -> None:
        self.send_metrics_repository = send_metrics_repository

    def incr(self, metric_name: str, action: str, metric_value: int) -> None:
        self.send_metrics_repository.metric_incr(metric_name, action, metric_value)

    def timing(self, metric_name: str, action: str, time_duration: int) -> None:
        self.send_metrics_repository.metric_timing(metric_name, action, time_duration)
