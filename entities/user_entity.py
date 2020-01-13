import sys
from flask_restful import Resource
from flask import request

sys.path.append('/home/pawan/PycharmProjects/StudentApp')
from usecases.user_usecase import signin, register


# registering new user 
class UserRegister(Resource):
    def post(self):
        data = request.get_json()
        res = register(data)
        return res


# signing in existing user
class SignIn(Resource):
    def get(self):
        data = request.get_json()
        res = signin(data)
        return res