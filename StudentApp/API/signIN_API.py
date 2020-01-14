import jwt
from flask_restful import Resource
from flask import request

class SignIn(Resource):
    def get(self):
        data = request.get_json()
        usr=valid_user(data['username'],data['password'])
        if(usr):
            byte_token = jwt.encode({"username":data['username'],"email":data['email'],"role":data['role']},secret_key,algorithm='HS256')
            string_token=byte_token.decode('UTF-8')
            return {"token":string_token}
        else:
            return {"message":"invalid credentials"}