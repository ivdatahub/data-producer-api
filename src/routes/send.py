from flask import Blueprint, request
from src.controller.send_controller import send

send_bp = Blueprint('send', __name__)


@send_bp.route('/', methods=['POST'])
def send_route():
    data = request.get_json()
    return send(data)
