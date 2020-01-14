import sys
import jwt
import bcrypt
from flask import request
secret_key = "secret108"
sys.path.append('/home/pawan/PycharmProjects/StudentApp')
from data_providers.db_operations import connect_database
from data_providers.db_operations import disconnect_database


# user registration
def valid_user(username, password):
    cur, con = connect_database('student')
    select_valid_user = "SELECT * FROM users WHERE username = %s"
    cur.execute(select_valid_user, (username,))
    row = cur.fetchone()
    disconnect_database(cur, con)

    if row:
        # if username is matching the authenticate password
        byte_password = password.encode('UTF-8')
        byte_db_password = row[1].encode('UTF-8')
        user = bcrypt.checkpw(byte_password, byte_db_password)
        return user
    else:
        user = False
        return user


# sign in by the existing user
def signin(data):
    usr = valid_user(data['username'], data['password'])
    if (usr):
        byte_token = jwt.encode({"username": data['username'], "email": data['email'], "role": data['role']},
                                secret_key, algorithm='HS256')
        string_token = byte_token.decode('UTF-8')
        return {"token": string_token}
    else:
        return {"message": "invalid credentials"}


def register(data):
    data = request.get_json()
    cur, con = connect_database('student')
    insert_user = "INSERT INTO users(username, password, email, role) VALUES(%s, %s, %s, %s)"
    # passwords should not be stored as plain text in the database hence bcrypting(hashing) using some random salt
    # converting password to byte type since bcrypt accept byte type data
    byte_password = data["password"].encode('UTF-8')
    hashed_byte_password = bcrypt.hashpw(byte_password, bcrypt.gensalt())
    # converting password to hashed string type to store in database
    hashed_string_password = hashed_byte_password.decode('UTF-8')
    values = (data['username'], hashed_string_password, data['email'], data['role'])

    cur.execute(insert_user, values)
    disconnect_database(cur, con)
    return {"message": "user added successfully"}, 201