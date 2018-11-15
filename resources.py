from flask_restful import Resource, reqparse
from models import User

parser = reqparse.RequestParser()


# create
class Post(Resource):
    @staticmethod
    def post():

        parser.add_argument('username')
        parser.add_argument('email')
        response = parser.parse_args()
        try:
            User.add_to_db(response)
            return {
                'username': response['username'],
                'email': response['email']
            }, 200
        except Exception as exception_message:
            return {
                'err_message': exception_message.args,
            }, 400


# read
class Get(Resource):
    @staticmethod
    def get(response):
        try:
            db_row = User.get_row(response)
            return {
                'first': f'this is the users email, ({db_row.email})',
                'second': f'this is the users username, ({db_row.username})'
            }, 200
        except Exception as exception_message:
            return {
                'err_message': exception_message.args,
            }, 400


# update
class Put(Resource):
    @staticmethod
    def put():
        # update the email
        parser.add_argument('username')
        parser.add_argument('new_email')
        response = parser.parse_args()
        try:
            User.update_db(response)

            return {
                'username': response['username'],
                'email': response['new_email']
            }, 200
        except Exception as exception_message:
            return {
                'err_message': exception_message.args,
            }, 400


# delete
class Delete(Resource):
    @staticmethod
    def delete():
        parser.add_argument('username')
        response = parser.parse_args()
        try:
            User.delete_from_db(response)
            return {'message': 'successful'}

        except Exception as exception_message:
            return {
                'err_message': exception_message.args,
            }, 400
