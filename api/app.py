from flask import Blueprint
from flask_restful import Api

from api.getResources import GetResources

# creates a Blueprint for api
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
# ‘/<int:cloud_connector>/getResources’ URL is bound with resources(cloud_connector) function.
api.add_resource(GetResources, '/<int:cloud_connector>/getResources')
