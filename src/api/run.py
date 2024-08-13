import os
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from src.api.application.controller.send_controller import send
from src.api.application.use_cases.send_metrics import SendMetricsUseCase


def application_setup():
    if not os.getenv("env"):
        os.environ["env"] = "test"

    app = FastAPI()
    app.title = "data-producer-api"
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Allowed domains
        allow_credentials=True,
        allow_methods=["GET", "POST"],  # Only allow GET requests
        allow_headers=[
            "Authorization",
            "Content-Type",
        ],  # Allow the Authorization and Content-Type header
    )

    return app


app = application_setup()
send_metrics = SendMetricsUseCase()


@app.get("/ping")
async def ping():
    send_metrics.incr(metric_name="data_producer_api", action="ping", metric_value=1)
    return {"message": "pong"}


@app.post("/send")
async def send_route(request: Request):
    send_metrics.incr(
        metric_name="data_producer_api", action="received_request", metric_value=1
    )

    try:
        body = await request.json()
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid request body")

    return send(body)
