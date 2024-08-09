from src.api.application.services.get_metrics_server_address import (
    GetSecretValueService,
)
from src.api.adapters.secret_manager import SecretManagerAdapter


def get_metrics_server_address() -> str:
    repository = SecretManagerAdapter(secret_id="datadog-agent-server-address")
    metrics_server = GetSecretValueService.get(get_repository=repository)

    return metrics_server
