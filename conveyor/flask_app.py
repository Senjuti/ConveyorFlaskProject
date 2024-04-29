#!/usr/bin/env python

import logging

from flask import Flask, Blueprint, redirect
from flask_restx import Api

# from conveyor.routes.aws import aws_api
from conveyor.routes.register import register_api
from conveyor.routes.status import status_api

log = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s'
)

vanilla_blueprint = Blueprint('Vanilla Blueprint', __name__)
# blueprint = Blueprint('Conveyor API', __name__, url_prefix='/api/v1')
register_blp = Blueprint(
    'Login / Registration', __name__, url_prefix='/api/v1'
)
api = Api(register_blp, title='Conveyor API', description='CRUD API')
# api.add_namespace(aws_api)
api.add_namespace(register_api)
api.add_namespace(status_api)


def create_app():
    app = Flask(__name__)
    # app.register_blueprint(blueprint)
    app.register_blueprint(vanilla_blueprint)
    app.register_blueprint(register_blp)
    log.info(f'URL Map: {app.url_map}')
    return app


@vanilla_blueprint.route('/', methods=['GET'])
def api_root_redirect():
    """Redirect root / to /api"""
    return redirect('/api/v1')
