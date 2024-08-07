from abc import ABC, abstractmethod


class ISendApiData(ABC):
    @staticmethod
    @abstractmethod
    def send_data(data: dict):
        pass
