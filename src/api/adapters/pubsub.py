import json
from google.cloud import pubsub_v1
from fastapi import HTTPException
from src.api.application.ports.send_api_data import ISendApiData
from src.api.application.utils.contants import PROJECT_ID
import threading


class PubSub(ISendApiData):
    @staticmethod
    def send_data(data: dict, metrics):
        data_str = json.dumps(data)
        message = data_str.encode("utf-8")

        publisher = pubsub_v1.PublisherClient()
        topic_name = f"projects/{PROJECT_ID}/topics/gcp-streaming-pipeline"

        try:
            future = publisher.publish(topic_name, data=message)
        except Exception:
            raise HTTPException(
                status_code=500, detail="Error sending message to Pub/Sub topic"
            )

        if not future.result():
            raise HTTPException(
                status_code=500, detail="Error sending message to Pub/Sub topic"
            )

        metrics.execute("data_producer_api.sent_message", 1)

        return {"status": "success", "message_id": future.result()}
