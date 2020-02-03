import sys
from flask import request
from flask_restful import reqparse
sys.path.append('/home/pawan/PycharmProjects/StudentApp')
from data_providers.db_operations import fetch_studentName_db, add_student_db, delete_student_db, update_student_db, fetch_allStudents_db
from usecases.auth_usecase import jwt_required


def get_student():
    token = request.headers.get('Authorization')
    jwt_response = jwt_required(token)

    if (type( jwt_response) is tuple):

        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument("rollno", type=int, required=True, help="student roll no required to fetch the details")
        args = parser.parse_args()
        res = fetch_studentName_db(args['rollno'])

        return res
    else:
        return {"authentication": jwt_response}, 401


def add_student():
    token = request.headers.get('Authorization')
    jwt_response = jwt_required(token)

    if (type( jwt_response) is tuple):

        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument("rollno", type=int, required=True, help="student Roll No required to add the details into DB")
        parser.add_argument("name", type=str, required=True, help="student name required to add the details into DB")
        parser.add_argument("age", type=int, required=True, help="student age required to add the details into DB")
        parser.add_argument("branch", type=str, required=True, help="student branch required to add the details into DB")
        args = parser.parse_args()

        res = add_student_db((args['rollno'], args['name'], args['age'], args['branch']))
        return res
    else:
        return {"authentication": jwt_response}, 401


def delete_student():
    token = request.headers.get('Authorization')
    jwt_response = jwt_required(token)

    if (type( jwt_response) is tuple):

        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument("rollno", type=int, required=True, help="student Roll No required to delete the info")
        args = parser.parse_args()

        res = delete_student_db((args['rollno'],))
        return res
    else:
        return {"authentication": jwt_response}, 401


def update_student():
    token = request.headers.get('Authorization')
    jwt_response = jwt_required(token)

    if (type( jwt_response) is tuple):

        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument("rollno", type=int, required=True, help="Roll No required")
        parser.add_argument("branch", type=str, required=True, help="branch required")
        args = parser.parse_args()

        res = update_student_db((args['branch'], args['rollno']))
        return res
    else:
        return {"authentication": jwt_response}, 401

def get_students():

    token = request.headers.get('Authorization')
    jwt_response = jwt_required(token)
    if (type(jwt_response) is tuple):
        res = fetch_allStudents_db()
        return res
    else:
        return {"authentication": jwt_response}, 401





