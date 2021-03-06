from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request, url_for, redirect
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
api = Api(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

import resources
# from models import User
# from models import User

api.add_resource(resources.Post, '/post')
api.add_resource(resources.Get, '/get/<string:response>')
api.add_resource(resources.Put, '/put')
api.add_resource(resources.Delete, '/delete')

api.add_resource(resources.Users, '/users')
api.add_resource(resources.Users_goto, '/users/<int:id>')

if __name__ == "__main__":

    app.run()