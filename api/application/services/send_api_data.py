from api.application.ports.send_api_data import ISendApiData
from typing import Type
from fastapi import Request, HTTPException


class SendService:
    @staticmethod
    def send(send_repository: Type[ISendApiData], request_body: dict) -> dict:
        try:
            data = request_body
        except Exception as e:
            raise HTTPException(status_code=400, detail="Invalid JSON format")

        send = send_repository.send_data(data=request_body)

        if send["status"] == "success":
            return {"status": "ok"}
        else:
            raise HTTPException(status_code=502, detail="Error sending API data")





