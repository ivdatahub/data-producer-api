from abc import ABC, abstractmethod


class ISendMetrics(ABC):
    @abstractmethod
    def __init__(self) -> None:
        pass

    def metric_incr(self, metric_name: str, action: str, metric_value: int) -> None:
        pass

    def metric_timing(self, metric_name: str, action: str, time_duration: int) -> None:
        pass
