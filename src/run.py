from fastapi import FastAPI, Request
from src.application.controller.send_controller import send

app = FastAPI()


@app.get("/ping")
async def ping():
    return {"message": "pong"}


@app.post("/send")
async def send_route(request: Request):
    body = await request.json()
    response = send(body)
    return response
