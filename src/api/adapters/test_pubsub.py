import json
from unittest.mock import patch, MagicMock
from src.api.adapters.pubsub import PubSub


def test_send_data(mocker):
    mock_publisher_client = mocker.patch('google.cloud.pubsub_v1.PublisherClient')
    mock_publish = mock_publisher_client.return_value.publish
    mock_future = MagicMock()
    mock_future.result.return_value = 'mock_message_id'
    mock_publish.return_value = mock_future

    data = {"key": "value"}
    result = PubSub.send_data(data)

    assert result["status"] == "success"
    assert result["message_id"] == "mock_message_id"
    mock_publish.assert_called_once_with(
        "projects/ivanildobarauna/topics/gcp-streaming-pipeline",
        data=json.dumps(data).encode('utf-8')
    )
