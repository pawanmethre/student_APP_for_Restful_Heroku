import psycopg2
import bcrypt
import jwt
from flask import request
from flask_restful import Resource
from auth import secret_key



def valid_user(username,password):
    con = psycopg2.connect(database='student',user='postgres',password='108',port='5432',host='127.0.0.1')
    cur = con.cursor()
    select_valid_user = "SELECT * FROM users WHERE username = %s"
    cur.execute(select_valid_user, (username,))
    row = cur.fetchone()
    cur.close()
    con.close()

    if row:
        # if username is matching the authenticate password
        byte_password = password.encode('UTF-8')
        byte_db_password = row[1].encode('UTF-8')
        user=bcrypt.checkpw(byte_password, byte_db_password)
        return user
    else:
        user = False
        return user



class UserRegister(Resource):

    def post(self):
        data = request.get_json()
        con = psycopg2.connect(port='5432',host='127.0.0.1',database='student',user='postgres',password='108')
        cur = con.cursor()
        insert_user = "INSERT INTO users(username, password, email, role) VALUES(%s, %s, %s, %s)"
        # passwords should not be stored as plain text in the database hence bcrypting(hashing) using some random salt
        # converting password to byte type since bcrypt accept byte type data
        byte_password = data["password"].encode('UTF-8')
        hashed_byte_password = bcrypt.hashpw(byte_password, bcrypt.gensalt())
        # converting password to hashed string type to store in database
        hashed_string_password = hashed_byte_password.decode('UTF-8')
        values = (data['username'], hashed_string_password, data['email'], data['role'])

        cur.execute(insert_user, values)
        con.commit()
        cur.close()
        con.close()
        return {"message": "user added successfully"}, 201