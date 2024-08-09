import os

from fastapi import FastAPI, Request, HTTPException
from src.api.application.controller.send_controller import send
from src.api.application.use_cases.send_metrics import SendMetricsUseCase

if not os.getenv("env"):
    os.environ["env"] = "test"

app = FastAPI()

send_metrics = SendMetricsUseCase()


@app.get("/ping")
async def ping():
    send_metrics.execute("data_producer_api.ping", 1)
    return {"message": "pong"}


@app.post("/send")
async def send_route(request: Request):
    send_metrics.execute("data_producer_api.received_request", 1)

    try:
        body = await request.json()
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid request body")

    return send(body)
