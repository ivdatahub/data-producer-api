from src.api.application.services.send_metrics import SendMetricsService
from src.api.adapters.datadog_adapter import DataDogAdapter
from src.api.application.utils.singleton import Singleton


class SendMetricsUseCase(Singleton):
    def __init__(self) -> None:
        if not hasattr(self, "initialized"):
            self.metrics_repository = DataDogAdapter()
            self.send_metrics_service = SendMetricsService(self.metrics_repository)
            self.initialized = True

    def incr(self, metric_name: str, action: str, metric_value: int) -> None:
        self.send_metrics_service.incr(metric_name, action, metric_value)

    def timing(self, metric_name: str, action: str, time_duration: int) -> None:
        self.send_metrics_service.timing(metric_name, action, time_duration)
