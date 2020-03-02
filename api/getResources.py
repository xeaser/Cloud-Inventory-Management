from flask_restful import Resource, abort

from Base.apiWrapper import importApi
from Exceptions.ConnectorException import NotSupportedException


# getResources API for cloud connectors
class GetResources(Resource):
    # get HTTP verb for getResources API of each Cloud Connector supported
    def get(self, cloud_connector):
        try:
            if 1 <= cloud_connector <= 3:
                return {"regions": importApi(cloud_connector)}
            else:
                raise NotSupportedException
        except NotSupportedException:
            abort(400, message="Not Supported")
