from src.api.application.services.send_api_data import SendService
from src.api.adapters.pubsub import AppQueueAdapter


def send(request_body: dict):
    response = SendService.send(
        send_repository=AppQueueAdapter, request_body=request_body
    )

    return response
