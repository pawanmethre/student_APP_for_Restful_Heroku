import psycopg2
from flask import request
from flask_restful import Resource
from auth import jwt_required


class Students(Resource):
    def get(self):
        token = request.headers.get('Authorization')
        jwt = jwt_required(token)
        if (jwt):
            l=[]
            con = psycopg2.connect(database='student', host='127.0.0.1',port='5432',user='postgres',password='108')
            cur = con.cursor()
            select_student="SELECT * FROM students"
            cur.execute(select_student)
            rows=cur.fetchall()
            cur.close()
            con.close()
            for row in rows:
                l.append({"rollno":row[0], "name":row[1], "age":row[2], "branch":row[3]})
            return {"students":l},200
        else:
            return {"message": "authentication failed"}, 401