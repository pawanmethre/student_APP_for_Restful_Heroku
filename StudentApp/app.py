from flask import Flask
from flask_restful import Resource, Api
from API.student_API import Student
from API.user_Register_API import UserRegister
from API.students_API import Students
from API.signIN_API import SignIn


app = Flask(__name__)
api = Api(app)


api.add_resource(Student, '/student')
api.add_resource(UserRegister, '/register')
api.add_resource(SignIn, '/signIn')
api.add_resource(Students, '/students')

if __name__ == '__main__':
    app.run(debug=True)
