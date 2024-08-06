from src.api.application.services.send_api_data import SendService
from src.api.adapters.pubsub import PubSub


def send(request_body: dict, metrics):
    response = SendService.send(
        send_repository=PubSub, request_body=request_body, metrics=metrics
    )

    return response
