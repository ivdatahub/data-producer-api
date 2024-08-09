from src.api.application.services.send_metrics import SendMetricsService
from src.api.adapters.datadog import DataDogAdapter
from src.api.application.utils.singleton import Singleton


class SendMetricsUseCase(Singleton):
    def __init__(self) -> None:
        if not hasattr(self, "initialized"):
            self.metrics_repository = DataDogAdapter()
            self.send_metrics_service = SendMetricsService(self.metrics_repository)
            self.initialized = True

    def execute(self, metric_name: str, metric_value: int) -> None:
        self.send_metrics_service.send(metric_name, metric_value)
