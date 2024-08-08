from src.api.application.services.send_metrics import SendMetricsService
from src.api.adapters.datadog import DataDogAdapter


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)

        return cls._instance


class SendMetricsUseCase(Singleton):
    def __init__(self) -> None:
        if not hasattr(self, "initialized"):
            self.metrics_repository = DataDogAdapter()
            self.send_metrics_service = SendMetricsService(self.metrics_repository)
            self.initialized = True

    def execute(self, metric_name: str, metric_value: int) -> None:
        self.send_metrics_service.send(metric_name, metric_value)
