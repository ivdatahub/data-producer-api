import json
import queue
import threading
from google.cloud import pubsub_v1
from fastapi import HTTPException
from src.api.application.ports.send_api_data import ISendApiData
from src.api.application.utils.contants import PROJECT_ID
from src.api.application.use_cases.send_metrics import SendMetricsUseCase

app_queue = queue.Queue()


class AppQueueAdapter(ISendApiData):
    @staticmethod
    def send_data(data: dict):
        def queue_publisher():
            app_queue.put(data)

        def queue_consumer():
            metrics = SendMetricsUseCase()
            while True:
                data = app_queue.get()

                print(f"processing...{data}")
                PubSub.publish(data)
                metrics.execute("data_producer_api.sent_message", 1)
                print(f"finish...{data}")

                if app_queue.qsize() == 0:
                    app_queue.task_done()
                    print("the queue is empty")
                    break

        thread_queue_publisher = threading.Thread(target=queue_publisher)
        thread_queue_consumer = threading.Thread(target=queue_consumer)

        thread_queue_publisher.start()
        thread_queue_consumer.start()
        thread_queue_publisher.join()


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
