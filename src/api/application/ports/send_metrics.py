from abc import ABC, abstractmethod


class ISendMetrics(ABC):
    @abstractmethod
    def __init__(self) -> None:
        pass

    def send_metric(self, metric_name: str, metric_value: int) -> None:
        pass
