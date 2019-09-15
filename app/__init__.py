from flask import Flask
from .core.config import config


def create_app(env):
    """Create an application instance"""
    app = Flask(__name__)
    app.config.from_object(config[env])

    from .main import main
    app.register_blueprint(main)

    return app
