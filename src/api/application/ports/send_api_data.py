from abc import ABC


class ISendApiData(ABC):
    def __init__(self, data: dict):
        pass

    def send_data(self):
        pass
