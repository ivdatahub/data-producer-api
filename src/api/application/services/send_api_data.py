from src.api.application.ports.send_api_data import ISendApiData
from typing import Type
from fastapi import HTTPException
from fastapi.responses import JSONResponse


class SendService:
    @staticmethod
    def send(send_repository: Type[ISendApiData], request_body: dict) -> dict:
        send_repository(data=request_body).send_data()

        return JSONResponse(content={"message": "sent"}, status_code=201)
