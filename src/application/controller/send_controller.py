from src.application.services.send_api_data import SendService
from src.adapters.pubsub import PubSub


def send(request_body: dict):
    response = SendService.send(send_repository=PubSub, request_body=request_body)

    return response
