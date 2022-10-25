from flask import Flask,url_for
from flask_wtf.csrf import CSRFProtect, CSRFError
from .routes.utils import blueprints
from app.routes.api import api


def create_app(config_file='config.py'):
    app = Flask(__name__)
    csrf = CSRFProtect(app)
    register_extensions(app)
    register_blueprints(app)
    app.config.from_pyfile(config_file)
    return app


def register_extensions(app):
    api.init_app(app)


def register_blueprints(app):
    for blueprint in blueprints:
        app.register_blueprint(blueprint)

