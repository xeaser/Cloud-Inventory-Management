from flask_restful import Resource, abort

from Base.common import enums
from Exceptions.ConnectorException import NotSupportedException


# getResources API for cloud connectors
class GetResources(Resource):
    # get HTTP verb for getResources API of each Cloud Connector supported
    def get(self, cloud_connector):
        try:
            if cloud_connector < 1 or cloud_connector > 3:
                raise NotSupportedException
            connector = enums.CloudConnectors(cloud_connector)
            return {"message": "Hello, " + connector.name}
        except NotSupportedException:
            abort(400, message="Not Supported")
