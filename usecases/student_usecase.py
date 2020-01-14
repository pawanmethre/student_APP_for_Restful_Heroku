import jwt
import sys
from flask import request
secret_key = "secret108"
sys.path.append('/home/pawan/PycharmProjects/StudentApp')
from data_providers.db_operations import connect_database
from data_providers.db_operations import disconnect_database



# authenticating wether the user is valid or not by accessing user from jwt token
def jwt_required(token):
    payload = jwt.decode(token, secret_key, algorithm='HS256')
    cur, con = connect_database('student')
    verify_user = "SELECT * FROM users WHERE username=%s"
    cur.execute(verify_user, payload['username'])
    row = cur.fetchone()
    disconnect_database(cur, con)
    return row


def get_student(token, data):

    jwt = jwt_required(token)
    if (jwt):

        cur, con = connect_database('student')
        insert_stud = "SELECT * FROM students WHERE rollno=%s"
        values = (data['rollno'],)
        cur.execute(insert_stud,values)
        row = cur.fetchone()
        disconnect_database(cur, con)
        if(row):
            return {"rollno":row[0], "name":row[1], "age":row[2], "branch":row[3]},200
        else:
            return  {"message":"rollno doesnt exists"},404
    else:
        return {"message":"invalid signature"},401


def add_student(token, data):
    jwt = jwt_required(token)
    if (jwt):
        data = request.get_json()
        cur, con = connect_database('student')
        insert_stud = "INSERT INTO students(rollno, name, age, branch) VALUES(%s,%s, %s,%s)"
        values = (data['rollno'], data['name'], data['age'], data['branch'])
        cur.execute(insert_stud, values)
        disconnect_database(cur, con)
        return {"message": "student added successfully"}, 201
    else:
        return {"message": "authentication failed"}, 401


def delete_student(token, data):
    jwt = jwt_required(token)
    if (jwt):
        data = request.get_json()
        cur, con = connect_database('student')
        insert_stud = "DELETE FROM students WHERE rollno=%s"
        values = (data['rollno'],)
        cur.execute(insert_stud, values)
        disconnect_database(cur, con)
        return {"message": "student deleted successfully"}, 200
    else:
        return {"message": "invalid signature"}, 401


def update_student(token, data):
    jwt = jwt_required(token)
    if (jwt):
        data = request.get_json()
        cur, con = connect_database('student')
        insert_stud = "UPDATE students SET branch=%s WHERE rollno=%s"
        values = (data['branch'], data['rollno'])
        cur.execute(insert_stud, values)
        disconnect_database(cur, con)
        return {"message": "student branch updated successfully"}, 200
    else:
        return {"message": "invalid signature"}, 401


def get_students(token):
    jwt = jwt_required(token)
    if (jwt):
        l = []
        cur, con = connect_database('student')
        select_student = "SELECT * FROM students"
        cur.execute(select_student)
        rows = cur.fetchall()
        disconnect_database(cur, con)
        for row in rows:
            l.append({"rollno": row[0], "name": row[1], "age": row[2], "branch": row[3]})
        return {"students": l}, 200
    else:
        return {"message": "authentication failed"}, 401


