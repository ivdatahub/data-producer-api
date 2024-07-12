from src.application.services.send_api_data import SendService
from src.adapters.pubsub import PubSub


def send(request_body):
    response = SendService.send(send_repository=PubSub, request=request_body)

    return response
