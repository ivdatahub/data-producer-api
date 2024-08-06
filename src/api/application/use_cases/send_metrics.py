from src.api.application.services.send_metrics import SendMetricsService
from src.api.adapters.datadog import DataDogAdapter


class SendMetricsUseCase:
    def __init__(self) -> None:
        self.metrics_repository = DataDogAdapter()
        self.send_metrics_service = SendMetricsService(self.metrics_repository)

    def execute(self, metric_name: str, metric_value: int) -> None:
        self.send_metrics_service.send(metric_name, metric_value)
