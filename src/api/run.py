from fastapi import FastAPI, Request
from src.api.application.controller.send_controller import send
from src.api.application.use_cases.send_metrics import SendMetricsUseCase

app = FastAPI()

send_metrics = SendMetricsUseCase()


@app.get("/ping")
async def ping():
    send_metrics.execute("data_producer_api.ping", 1)
    return {"message": "pong"}


@app.post("/send")
async def send_route(request: Request):
    body = await request.json()
    response = send(body)
    return response
