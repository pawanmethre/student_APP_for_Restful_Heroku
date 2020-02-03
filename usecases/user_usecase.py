import time
import sys
import jwt
import bcrypt
from flask_restful import reqparse
secret_key = "secret108"
sys.path.append('/home/pawan/PycharmProjects/StudentApp')
from data_providers.db_operations import connect_database, disconnect_database, register_user, valid_user


def validate_user_credentials():
    parser = reqparse.RequestParser(bundle_errors=True)
    parser.add_argument("username", type=str, required=True, help="username required!")
    parser.add_argument("password", type=str, required=True, help="password required!")
    parser.add_argument("email", type=str, required=True, help="email required!")
    parser.add_argument("role", type=str, required=True, help="role required!")
    args = parser.parse_args()

    return args


# sign in by the existing user
def signin():

    args = validate_user_credentials()

    usr = valid_user(args['username'], args['password'])
    if (usr):
        # jwt expiry time set to 2 minute post authentication using time.time()+120
        byte_token = jwt.encode({"username": args['username'], "email": args['email'], "role": args['role'], 'exp': time.time()+120}, secret_key, algorithm='HS256')
        string_token = byte_token.decode('UTF-8')
        return {"token": string_token}
    else:
        return {"message": "invalid credentials"}


def register():

    args = validate_user_credentials()

    # passwords should not be stored as plain text in the database hence bcrypting(hashing) using some random salt
    # converting password to byte type since bcrypt accept byte type data
    byte_password = args["password"].encode('UTF-8')
    hashed_byte_password = bcrypt.hashpw(byte_password, bcrypt.gensalt())
    # converting password to hashed string type to store in database
    hashed_string_password = hashed_byte_password.decode('UTF-8')
    data = (args['username'], hashed_string_password, args['email'], args['role'])
    res = register_user(data)
    return res