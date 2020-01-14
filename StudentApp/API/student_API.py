import psycopg2
import jwt
from flask import  request
from flask_restful import Resource
from auth import jwt_required


class Student(Resource):

    def get(self):
        token = request.headers.get('Authorization')
        jwt = jwt_required(token)
        if (jwt):
            data = request.get_json()
            con = psycopg2.connect(user="postgres",database="student",password="108",port="5432",host="127.0.0.1")
            cur = con.cursor()
            insert_stud = "SELECT * FROM students WHERE rollno=%s"
            values = (data['rollno'],)
            cur.execute(insert_stud,values)
            row=cur.fetchone()
            cur.close()
            con.close()
            if(row):
                return {"rollno":row[0], "name":row[1], "age":row[2], "branch":row[3]},200
            else:
                return  {"message":"rollno doesnt exists"},404
        else:
            return {"message":"invalid signature"},401


    def post(self):
        token = request.headers.get('Authorization')
        jwt = jwt_required(token)
        if (jwt):
            data=request.get_json()
            con = psycopg2.connect(user="postgres",database="student",password="108",port="5432",host="127.0.0.1")
            cur = con.cursor()
            insert_stud = "INSERT INTO students(rollno, name, age, branch) VALUES(%s,%s, %s,%s)"
            values = (data['rollno'], data['name'], data['age'], data['branch'])
            cur.execute(insert_stud,values)
            con.commit()
            cur.close()
            con.close()
            return {"message":"student added successfully"},201
        else:
            return {"message":"authentication failed"},401

    def delete(self):
        token = request.headers.get('Authorization')
        jwt = jwt_required(token)
        if (jwt):
            data = request.get_json()
            con = psycopg2.connect(user="postgres", database="student", password="108", port="5432", host="127.0.0.1")
            cur = con.cursor()
            insert_stud = "DELETE FROM students WHERE rollno=%s"
            values = (data['rollno'],)
            cur.execute(insert_stud, values)
            con.commit()
            cur.close()
            con.close()
            return {"message":"student deleted successfully"}, 200
        else:
            return {"message": "invalid signature"}, 401

    def put(self):
        token = request.headers.get('Authorization')
        jwt = jwt_required(token)
        if (jwt):
            data = request.get_json()
            con = psycopg2.connect(user="postgres", database="student", password="108", port="5432", host="127.0.0.1")
            cur = con.cursor()
            insert_stud = "UPDATE students SET branch=%s WHERE rollno=%s"
            values = (data['branch'],data['rollno'])
            cur.execute(insert_stud, values)
            con.commit()
            cur.close()
            con.close()
            return {"message":"student branch updated successfully"}, 200
        else:
            return {"message": "invalid signature"}, 401