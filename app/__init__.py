from flask import Flask
from app.routes.views import home_blueprint
from flask_wtf.csrf import CSRFProtect,CSRFError


def create_app(config_file='config.py'):

    app = Flask(__name__)
    csrf = CSRFProtect(app)
    app.config.from_pyfile(config_file)
    BLUEPRINTS = [home_blueprint]

    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)


    return app
