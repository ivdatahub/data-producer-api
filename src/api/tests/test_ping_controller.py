from src.api.application.controller.ping_controller import ping


def test_ping_controller():
    assert ping() == ("pong", 200)
