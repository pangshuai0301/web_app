# -*- coding: utf-8 -*-

from flask import Flask, render_template
from config import config

def create_app(config_name):
    from .main import main as main_blueprint
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    app.register_blueprint(main_blueprint)

    return app
