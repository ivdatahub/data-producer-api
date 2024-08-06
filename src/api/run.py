from fastapi import FastAPI, Request
from src.api.application.controller.send_controller import send
from datadog import initialize, statsd


def client_options():
    """
    Returns the client options for the Datadog client.
    """
    options = {"statsd_host": "10.142.0.10", "statsd_port": 8125}

    return options


initialize(**client_options())

app = FastAPI()


@app.get("/ping")
async def ping():
    statsd.increment(metric="data-producer-api.ping", value=1)
    return {"message": "pong"}


@app.post("/send")
async def send_route(request: Request):
    body = await request.json()
    response = send(body)
    return response
