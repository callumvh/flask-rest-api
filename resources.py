from flask_restful import Resource, reqparse
from models import User
import json
from flask import jsonify

parser = reqparse.RequestParser()


# create
class Post(Resource):
    @staticmethod
    def post():

        parser.add_argument('username')
        parser.add_argument('email')
        parser.add_argument('password')
        response = parser.parse_args()
        try:
            User.add_to_db(response)
            return {
                'username': response['username'],
                'email': response['email'],
                'password': response['password'],
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


def put_users_json():
    json_return = {"count": None, "results": []}
    # results_list = []
    each_person_dict = {
        "url": None,
        "id": None,
        "username": None,
        "email": None
    }
    list_of_rows = User.get_row_by_id()
    json_return["count"] = len(list_of_rows)

    for x in range(0, len(list_of_rows)):
        # print()
        #
        each_person_dict = {}
        print(list_of_rows[x].username)
        each_person_dict["username"] = list_of_rows[x].username
        each_person_dict["email"] = list_of_rows[x].email
        each_person_dict["id"] = x
        # each_person_dict["rel"] = f'http://localhost:5000/users/{x}'
        each_person_dict["links"] = {
            "type": "GET",
            "rel": f'http://localhost:5000/users/{x}'
        }

        print(each_person_dict)
        json_return["results"].append(each_person_dict)
        # json_return["results"][x]["username"] = list_of_rows[x].username
    return json_return


class Users(Resource):
    @staticmethod
    def get():
        json_return = put_users_json()

        x = json_return
        print(json.dumps(x, indent=2))
        return json_return


class Users_goto(Resource):
    @staticmethod
    def get(id):
        json_return = put_users_json()
        new_json = {}
        list_person = json_return["results"]
        final_dict = list_person[id]

        final_dict.pop('links')
        return final_dict
