from datadog import initialize, statsd
import time
import random


def client_options():
    options = {"statsd_host": "localhost", "statsd_port": 8125}

    return options


initialize(**client_options())

total_increments = 100


def send_metrics():
    for i in range(total_increments):
        print(f"Sending metric {i + 1} of {total_increments}")
        statsd.increment(
            metric="local_metric", value=random.randint(50, 100), tags=["env:test"]
        )
        time.sleep(random.randint(0, 10))

    print("Metrics sent successfully!")


if __name__ == "__main__":
    send_metrics()
