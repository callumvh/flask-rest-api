# pylint: disable=E1101
from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=True, nullable=False)

    @staticmethod
    def add_to_db(response):
        db.session.add(
            User(
                username=response['username'],
                email=response['email'],
                password=response['password'],
            ))
        db.session.commit()

    @staticmethod
    def update_db(response):
        db_name = User.query.filter_by(username=response['username']).first()
        db_name.email = response['new_email']
        db.session.commit()

    @staticmethod
    def get_row(response):
        the_row = User.query.filter_by(username=response).first()
        return the_row

    @staticmethod
    def delete_from_db(response):
        name = response['username']
        row = User.query.filter_by(username=name).first()
        db.session.delete(row)
        db.session.commit()

    @staticmethod
    def get_row_by_id():
        all_data = User.query.order_by(User.id).all()
        return all_data
