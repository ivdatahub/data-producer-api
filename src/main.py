import time
import random

from datadog import initialize, statsd


def client_options():
    """
    Returns the client options for the Datadog client.
    """
    options = {"statsd_host": "localhost", "statsd_port": 8125}

    return options


try:
    initialize(**client_options())
except Exception as e:
    print(f"Error initializing client: {e}")
    raise e


def send_metrics():
    """
    Send metrics to Datadog.
    """
    total_increments = 1000000
    for i in range(total_increments):
        random_value = random.randint(50, 100)
        print(f"Sending metric {i + 1} of {total_increments}")
        statsd.increment(metric="local_metric", value=random_value)

        time.sleep(random.randint(0, 10))

    print("Metrics sent successfully!")


if __name__ == "__main__":
    send_metrics()
