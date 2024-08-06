import time
import random
from src.api.application.use_cases.send_metrics import SendMetricsUseCase

send_metrics = SendMetricsUseCase()


def execute():
    """
    Send metrics to Datadog.
    """
    total_increments = 1000000
    for i in range(total_increments):
        random_value = random.randint(50, 100)
        print(f"Sending metric {i + 1} of {total_increments}")
        send_metrics.execute("local_metric", random_value)

        time.sleep(random.randint(0, 10))

    print("Metrics sent successfully!")


if __name__ == "__main__":
    execute()
