import json
from unittest.mock import patch, MagicMock
from src.api.adapters.pubsub_adapter import PubSub


def test_send_data(mocker):
    mock_publisher_client = mocker.patch("google.cloud.pubsub_v1.PublisherClient")
    mock_publish = mock_publisher_client.return_value.publish
    mock_future = MagicMock()
    mock_future.result.return_value = "mock_message_id"
    mock_publish.return_value = mock_future

    data = {"key": "value"}
    result = PubSub.publish(data)

    assert result["message_id"] == "mock_message_id"
    mock_publish.assert_called_once_with(
        "projects/data-producer-api/topics/gcp-streaming-pipeline",
        data=json.dumps(data).encode("utf-8"),
    )
