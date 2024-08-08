import json
import queue
from google.cloud import pubsub_v1
from fastapi import HTTPException
from src.api.application.ports.send_api_data import ISendApiData
from src.api.application.utils.contants import PROJECT_ID
from src.api.application.use_cases.send_metrics import SendMetricsUseCase
import concurrent.futures


class AppQueueAdapter(ISendApiData):
    def __init__(self, data: dict):
        self.executor = concurrent.futures.ThreadPoolExecutor()
        self.data = data
        self.metrics = SendMetricsUseCase()
        self.app_queue = AppQueue().get_queue()

    def send_data(self):
        self.executor.submit(self.queue_publisher)
        self.executor.submit(self.queue_consumer)

    def queue_publisher(self):
        self.app_queue.put(self.data)

    def queue_consumer(self):
        while True:
            self.metrics.execute(
                "data_producer_api.app_queue_size", self.app_queue.qsize()
            )
            data = self.app_queue.get()

            PubSub.publish(data)
            self.metrics.execute("data_producer_api.sent_message", 1)
            self.app_queue.task_done()

            if self.app_queue.qsize() == 0:
                break


class PubSub:
    @staticmethod
    def publish(data: dict):
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


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)

        return cls._instance


class AppQueue(Singleton):
    def __init__(self) -> None:
        if not hasattr(self, "initialized"):
            self.app_queue = queue.Queue()
            self.initialized = True

    def get_queue(self):
        return self.app_queue
