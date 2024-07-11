from src.application.services.send_api_data import SendService
from src.adapters.pubsub import PubSub


def send(request):
    response = SendService.send(send_repository=PubSub, request=request)

    return response
