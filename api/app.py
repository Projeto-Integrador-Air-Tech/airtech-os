import logging
from flask import Flask
from flask_restful import Api
from cheroot.wsgi import Server as WSGIServer
from api.routes.funcionarios import FuncionariosResource


APP = Flask(__name__)
API = Api(APP)
PORT = 8080
SERVER = WSGIServer(('0.0.0.0', PORT), APP)

API.add_resource(FuncionariosResource, '/funcionarios', '/funcionarios/<int:id>')


if __name__ == '__main__':
    logging.basicConfig(format='', level=logging.INFO)
    logging.info('Running server on port %s', PORT)
    SERVER.safe_start()