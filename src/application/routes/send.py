from flask import Blueprint, request
from src.application.controller.send_controller import send

send_bp = Blueprint('send', __name__)


@send_bp.route('/', methods=['POST'])
def send_route():
    return send(request)
