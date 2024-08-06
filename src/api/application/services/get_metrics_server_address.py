from src.api.application.ports.get_secrets import IGetSecrets
from typing import Type


class GetSecretValueService:
    @staticmethod
    def get(get_repository: Type[IGetSecrets]) -> dict:
        try:
            secret_value = get_repository.get_secret_value()
        except Exception as e:
            raise e

        return secret_value
