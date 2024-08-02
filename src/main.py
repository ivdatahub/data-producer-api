from datadog import initialize, statsd, get_hostname
import time
import random


def client_options():
    options = {"statsd_host": "localhost", "statsd_port": 8125}

    return options


try:
    initialize(**client_options())
except Exception as e:
    print(f"Error initializing client: {e}")
    raise e


def send_metrics():
    total_increments = 100
    for i in range(total_increments):
        random_value = random.randint(50, 100)
        print(f"Sending metric {i + 1} of {total_increments}")
        statsd.increment(metric="local_metric", value=random_value)

        time.sleep(random.randint(0, 10))

    print("Metrics sent successfully!")


if __name__ == "__main__":
    send_metrics()
