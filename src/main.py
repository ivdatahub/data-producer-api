import time
import random
from src.api.adapters.secret_manager import SecretManagerAdapter


from datadog import initialize, statsd

dd_server_address = SecretManagerAdapter(
    secret_id="datadog-agent-server-address"
).get_secret_value()


# def client_options():
#     """
#     Returns the client options for the Datadog client.
#     """
#     options = {"statsd_host": "10.142.0.10", "statsd_port": 8125}
#
#     return options
#
#
# initialize(**client_options())
#
#
# def send_metrics():
#     """
#     Send metrics to Datadog.
#     """
#     total_increments = 1000000
#     for i in range(total_increments):
#         random_value = random.randint(50, 100)
#         print(f"Sending metric {i + 1} of {total_increments}")
#         statsd.increment(metric="local_metric", value=random_value)

#         time.sleep(random.randint(0, 10))
#
#     print("Metrics sent successfully!")
#
#
# if __name__ == "__main__":
#     send_metrics()
