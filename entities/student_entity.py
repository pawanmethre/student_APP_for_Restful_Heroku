import sys
from flask import request
from flask_restful import Resource
sys.path.append('/home/pawan/PycharmProjects/StudentApp')
from usecases.student_usecase import get_student, add_student, delete_student,  update_student, get_students


class Student(Resource):
    # get particular student details
    def get(self):
        res = get_student()
        return res

    # add particular student details
    def post(self):
        res = add_student()
        return res

    # delete particular student details
    def delete(self):
        res = delete_student()
        return res

    # update branch of particular student
    def put(self):
        res = update_student()
        return res


class Students(Resource):

    # fetch details of all the students
    def get(self):
        res = get_students()
        return res