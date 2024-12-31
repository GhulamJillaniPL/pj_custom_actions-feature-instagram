import os
from typing import Optional

from flask import Flask, json
from werkzeug.exceptions import HTTPException
from werkzeug.routing import ValidationError

from .config import Config, get_config
from .instagram.views import blueprint as instagram_blueprint


def create_app(test_config: Optional[Config] = None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    if test_config:
        app.config.from_object(test_config)
    else:
        app.config.from_object(get_config())

    register_blueprints(app)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/api')
    def hello():
        return 'Welcome, Stranger'

    @app.route('/ping')
    def ping():
        # to check status of application
        return 'PONG'

    @app.errorhandler(404)
    @app.errorhandler(HTTPException)
    def handle_exception(e):
        """Return JSON instead of HTML for HTTP errors."""

        response = e.get_response()

        error_payload = {
            "code": e.code,
            "name": e.name,
        }
        if isinstance(e.description, ValidationError):
            error_payload['errors'] = e.description.normalized_messages()
        else:
            error_payload['description'] = e.description

        response.data = json.dumps(error_payload)
        response.content_type = "application/json"
        return response

    return app


def register_blueprints(app: Flask):
    # register all the blueprints here
    app.register_blueprint(instagram_blueprint, url_prefix="/api/instagram")

