from src.api.application.ports.get_secrets import IGetSecrets
from google.cloud import secretmanager
from src.api.application.utils.contants import PROJECT_ID


class SecretManagerAdapter(IGetSecrets):
    def __init__(self, secret_id: str) -> None:
        self.secret_id = secret_id

    def get_secret_value(self) -> str:
        secret_client = secretmanager.SecretManagerServiceClient()

        request = {
            "name": f"projects/{PROJECT_ID}/secrets/{self.secret_id}/versions/latest",
        }

        secret_request = secret_client.access_secret_version(request=request)

        return secret_request.payload.data.decode("UTF-8")
