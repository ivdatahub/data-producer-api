from abc import ABC, abstractmethod


class IGetSecrets(ABC):
    @abstractmethod
    def __init__(self, secret_id: str) -> None:
        pass

    def get_secret_value(self) -> str:
        pass
