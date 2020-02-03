from flask import Flask
from flask_restful import Api
import sys
sys.path.append('/home/pawan/PycharmProjects/StudentApp')
from entities.student_entity import Student, Students
from  entities.user_entity import SignIn, UserRegister


app = Flask(__name__)
api = Api(app)

api.add_resource(Student, '/student')
api.add_resource(UserRegister, '/auth/register')
api.add_resource(SignIn, '/auth/signIn')
api.add_resource(Students, '/student/students')

if __name__ == '__main__':
    app.run(debug=True)
