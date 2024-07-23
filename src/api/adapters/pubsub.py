import json
from src.api.application.ports.send_api_data import ISendApiData
from google.cloud import pubsub_v1


class PubSub(ISendApiData):
    @staticmethod
    def send_data(data: dict):
        data_str = json.dumps(data)
        message = data_str.encode('utf-8')

        publisher = pubsub_v1.PublisherClient()
        topic_name = "projects/ivanildobarauna/topics/gcp-streaming-pipeline"

        try:
            future = publisher.publish(topic_name, data=message)
        except Exception as e:
            print(f"Error sending message to Pub/Sub topic: {topic_name}")
            raise e

        if not future.result():
            return {
                "status": "error",
                "data": data,
                "future": future
            }

        return {
                "status": "success",
                "message_id": future.result()
            }