from flask_restful import Resource, abort

from Base.apiWrapper import importApi
# from Base.common.enums import CloudConnectors
from Exceptions.ConnectorException import NotSupportedException


# getResources API for cloud connectors
class GetResources(Resource):
    # get HTTP verb for getResources API of each Cloud Connector supported
    def get(self, cloud_connector):
        try:
            if cloud_connector < 1 or cloud_connector > 3:
                raise NotSupportedException
            return {"regions": importApi(cloud_connector)}
        except NotSupportedException:
            abort(400, message="Not Supported")
