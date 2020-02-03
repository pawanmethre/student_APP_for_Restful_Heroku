import sys
from flask_restful import Resource
from flask import request

sys.path.append('/home/pawan/PycharmProjects/StudentApp')
from usecases.user_usecase import signin, register


# registering new user 
class UserRegister(Resource):
    def post(self):
        res = register()
        return res


# signing in existing user
class SignIn(Resource):
    def get(self):
        res = signin()
        return res