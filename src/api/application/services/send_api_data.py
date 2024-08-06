from src.api.application.ports.send_api_data import ISendApiData
from typing import Type
from fastapi import HTTPException
import concurrent.futures


class SendService:
    @staticmethod
    def send(send_repository: Type[ISendApiData], request_body: dict, metrics) -> dict:
        try:
            data = request_body
        except Exception:
            raise HTTPException(status_code=400, detail="Invalid JSON format")

        def snd():
            send_repository.send_data(data=data, metrics=metrics)

        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.submit(snd)

        return {"status": "ok"}
