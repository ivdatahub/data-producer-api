import json
import queue
from datetime import datetime
from google.cloud import pubsub_v1
from fastapi import HTTPException
from src.api.application.ports.send_api_data import ISendApiData
from src.api.application.utils.contants import PROJECT_ID
from src.api.application.utils.singleton import Singleton
from src.api.application.use_cases.send_metrics import SendMetricsUseCase
import concurrent.futures


class AppQueueAdapter(ISendApiData):
    def __init__(self, data: dict):
        self.executor = concurrent.futures.ThreadPoolExecutor()
        self.data = data
        self.metrics = SendMetricsUseCase()
        self.app_queue = AppQueue().get_queue()

    def send_data(self):
        self.app_queue.put(self.data)
        self.executor.submit(self.queue_consumer)

    def queue_consumer(self):
        start_time = datetime.now()
        while True:
            self.metrics.execute(
                metric_name="data_producer_api",
                action="app_queue_size",
                metric_value=self.app_queue.qsize(),
            )
            data = self.app_queue.get()

            PubSub.publish(data)
            self.metrics.execute(
                metric_name="data_producer_api", action="sent_message", metric_value=1
            )
            self.app_queue.task_done()

            if self.app_queue.qsize() == 0:
                self.metrics.execute(
                    metric_name="data_producer_api",
                    action="consumer_time",
                    metric_value=(datetime.now() - start_time).microseconds,
                )
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

        return {"message_id": future.result()}


class AppQueue(Singleton):
    def __init__(self) -> None:
        if not hasattr(self, "initialized"):
            self.app_queue = queue.Queue()
            self.initialized = True

    def get_queue(self):
        return self.app_queue
