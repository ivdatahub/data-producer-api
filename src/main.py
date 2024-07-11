import os
from google.cloud import pubsub_v1


def send_message():
    try:
        publisher = pubsub_v1.PublisherClient()
        topic_name = "projects/ivanildobarauna/topics/gcp-streaming-pipeline"
        future = publisher.publish(topic_name, b'My first message!', spam='eggs')
    except Exception as e:
        return str(e)

    print("Published message ID: ", future.result())


def get_messages():
    subscription_name = "projects/ivanildobarauna/subscriptions/gcp-streaming-pipeline-sub"

    def callback(message):
        print(message.data)
        # message.ack()

    with pubsub_v1.SubscriberClient() as subscriber:
        future = subscriber.subscribe(subscription_name, callback)

    try:
        future.result()
        print("Received message: ", future.result())
    except KeyboardInterrupt:
        future.cancel()


if __name__ == "__main__":
    send_message()
