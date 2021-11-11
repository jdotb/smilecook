from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from http import HTTPStatus

from utils import hash_password
from models.user import User


class UserListResource(Resource):
    # POST method
    def post(self):
        json_data = request.get_json()

        username = json_data.get('username')
        email = json_data.get('email')
        non_hash_password = json_data.get('password')

        # Check whether user exists in db using get_by_username/get_by_email
        if User.get_by_username(username):
            return {'message': 'username already used'}, HTTPStatus.BAD_REQUEST

        if User.get_by_email(email):
            return {'message': 'email already used'}, HTTPStatus.BAD_REQUEST

        # create user in db
        password = hash_password(non_hash_password)

        user = User(
            username=username,
            email=email,
            password=password
        )
        user.save()

        data = {
            'id': user.id,
            'username': user.username,
            'email': user.email
        }

        return data, HTTPStatus.CREATED


class UserResource(Resource):
    # define GET method - @jwt_optional says that no token is required to access this endpoint
    @jwt_required(optional=True)
    def get(self, username):

        # check if username can be found in db
        user = User.get_by_username(username=username)

        if user is None:
            return {'message': 'user not found'}, HTTPStatus.NOT_FOUND

        # if user found, check if matches identity of user in JWT
        current_user = get_jwt_identity()

        # if user matches, apply access control
        if current_user == user.id:
            data = {
                'id': user.id,
                'username': user.username,
                'email': user.email
            }

        else:
            data = {
                'id': user.id,
                'username': user.username,
            }

        return data, HTTPStatus.OK


class MeResource(Resource):

    @jwt_required
    def get(self):
        user = User.get_by_id(id=get_jwt_identity())

        data = {
            'id': user.id,
            'username': user.username,
            'email': user.email
        }

        return data, HTTPStatus.OK
