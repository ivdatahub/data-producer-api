from src.application.ports.send_api_data import ISendApiData
from typing import Type
from flask import request, jsonify


class SendService:
    @staticmethod
    def send(send_repository: Type[ISendApiData], request: Type[request]) -> tuple:
        try:
            data = request.get_json()
        except Exception as e:
            jsonify({"status": "error"}, data), 400  # Bad Request

        send = send_repository.send_data(data=data)

        if send["status"] == "success":
            return jsonify(send), 200
        else:
            return jsonify(send), 502  # Bad Gateway





