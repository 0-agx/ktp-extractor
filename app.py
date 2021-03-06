from distutils.log import debug
from flask import Flask
from core.router import Router
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
Router.run(app)
