import sys
from flask import request
from flask_restful import Resource
sys.path.append('/home/pawan/PycharmProjects/StudentApp')
from usecases.student_usecase import get_student, add_student, delete_student,  update_student, get_students


class Student(Resource):
    # get particular student details
    def get(self):
        token = request.headers.get('Authorization')
        data = request.get_json()
        res = get_student(token, data)
        return res

    # add particular student details
    def post(self):
        token = request.headers.get('Authorization')
        data = request.get_json()
        res = add_student(token, data)
        return res

    # delete particular student details
    def delete(self):
        token = request.headers.get('Authorization')
        data = request.get_json()
        res = delete_student(token, data)
        return res

    # update branch of particular student
    def put(self):
        token = request.headers.get('Authorization')
        data = request.get_json()
        res = update_student(token, data)
        return res


class Students(Resource):

    # fetch details of all the students
    def get(self):
        token = request.headers.get('Authorization')
        res = get_students(token)
        return res
