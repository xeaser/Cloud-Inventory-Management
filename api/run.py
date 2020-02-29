#!flask/bin/python
# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask


def create_app():
    # Flask constructor takes the name of
    # current module (__name__) as argument.
    app = Flask(__name__)

    from api.app import api_bp
    # /api/v1 version api register the api blueprint
    app.register_blueprint(api_bp, url_prefix='/api/v1')

    return app


# main driver function
if __name__ == "__main__":
    # can be configured with a config file for dependency injection and clients
    webapp = create_app()
    # run() method of Flask class runs the application
    # on the local development server.
    webapp.run(debug=True)
