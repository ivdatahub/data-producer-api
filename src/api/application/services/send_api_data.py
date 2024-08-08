from src.api.application.ports.send_api_data import ISendApiData
from typing import Type
from fastapi import HTTPException
import concurrent.futures


class SendService:
    @staticmethod
    def send(send_repository: Type[ISendApiData], request_body: dict) -> dict:
        try:
            data = request_body
        except Exception:
            raise HTTPException(status_code=400, detail="Invalid JSON format")

        send_repository(data=data).send_data()

        return {"status": "ok"}
