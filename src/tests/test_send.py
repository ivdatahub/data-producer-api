import pytest
from src.app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_send_one_row(client):
    payload = {
        'email': 'aaa',
        'password': 'bbb'
        }
    response = client.post('/send/', json=payload)
    assert response.status_code == 200


def test_send_two_rows(client):
    payload = {
        'email': 'aaa',
        'password': 'bbb'
        }
    response = client.post('/send/', json=payload)
    assert response.status_code == 200
