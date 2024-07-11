from google.cloud import pubsub_v1
import threading


def send_message():
    try:
        publisher = pubsub_v1.PublisherClient()
        topic_name = "projects/ivanildobarauna/topics/gcp-streaming-pipeline"
        for i in range(1000000):
            future = publisher.publish(topic_name, b'send by send_message() in pyCharm!', env='test')
    except Exception as e:
        raise e


def get_messages():
    subscription_name = "projects/ivanildobarauna/subscriptions/gcp-streaming-pipeline-sub"

    def callback(message):
        print(message)
        message.ack()

    with pubsub_v1.SubscriberClient() as subscriber:
        future = subscriber.subscribe(subscription_name, callback)
        try:
            future.result()
        except KeyboardInterrupt:
            future.cancel()


if __name__ == "__main__":
    publisher_thread = threading.Thread(target=send_message)
    consumer_thread = threading.Thread(target=get_messages)

    publisher_thread.start()

    consumer_thread.start()
    consumer_thread.join()


