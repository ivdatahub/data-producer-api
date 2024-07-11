from flask import Flask
from src.application.routes.ping import ping_bp
from src.application.routes.send import send_bp


def create_app():
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(ping_bp, url_prefix='/ping')
    app.register_blueprint(send_bp, url_prefix='/send')

    return app


if __name__ == '__main__':  # pragma: no cover
    app = create_app()  # pragma: no cover
    app.run(host='0.0.0.0', port=8080)  # pragma: no cover
