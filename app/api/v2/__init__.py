from flask_restful import Api
from flask import Blueprint
from app.api.v2.test import Hello


def register_views(app):
    api = Api(app)
    api.add_resource(Hello, '/hello', endpoint="hello")

def  create_blueprint_v2():
    bp_v2 = Blueprint('v2', __name__)
    register_views(bp_v2)
    return bp_v2
