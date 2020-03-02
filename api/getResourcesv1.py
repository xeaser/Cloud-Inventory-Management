#!flask/bin/python
# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask
from flask import abort

from Base.common import enums
from Exceptions.ConnectorException import NotSupportedException

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)


# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/api/v1/<int:cloud_connector>/getResources', methods=["GET"])
# ‘/api/v1/<int:cloud_connector>/getResources’ URL is bound with resources(cloud_connector) function.
def resources(cloud_connector):
    try:
        if cloud_connector < 1 or cloud_connector > 3:
            raise NotSupportedException
        connector = enums.CloudConnectors(cloud_connector)
        return "Hello, " + connector.name
    except NotSupportedException:
        abort(400, "Not Supported")


# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(debug=True)
