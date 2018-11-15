from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request, url_for, redirect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
api = Api(app)
db = SQLAlchemy(app)

import resources
# from models import User
# from models import User

api.add_resource(resources.Post, '/post')
api.add_resource(resources.Get, '/get/<string:response>')
api.add_resource(resources.Put, '/put')
api.add_resource(resources.Delete, '/delete')