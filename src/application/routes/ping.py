from flask import Blueprint
from src.application.controller.ping_controller import ping

ping_bp = Blueprint('ping', __name__)


@ping_bp.route('/', methods=['GET'])
def ping_route():
    return ping()

