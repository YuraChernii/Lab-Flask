from gevent import monkey
monkey.patch_all()
from flask import Flask, request, make_response
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, ForeignKey
from flask import Flask,abort,session, jsonify
from flask_restful import Api, Resource, reqparse, fields, marshal_with
from sqlalchemy import func
#from gevent import wsgi
from gevent import pywsgi
from http import HTTPStatus
from json import dumps
from werkzeug.security import generate_password_hash, check_password_hash




app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc://HP-ПК/databasePython?driver=SQL+Server?trusted_connection=yes"
#app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc://yura:12345@HP-ПК/TestEFCore"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)
class Student(db.Model):
    __tablename__ = 'student'

    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String)
    admin = db.Column(db.Boolean)
    email = db.Column(db.String)
    phone = db.Column(db.String)
    password = db.Column(db.String)





class Marks(db.Model):
    __tablename__ = 'marks'

    id = db.Column(db.Integer, primary_key=True)
    studentId = db.Column(db.Integer, db.ForeignKey("student.id"))
    subjectName = db.Column(db.String)
    rating = db.Column(db.Integer)
migrate = Migrate(app, db)
#db.create_all()

from app import routes

student_put_args = reqparse.RequestParser()
student_put_args2 = reqparse.RequestParser()
student_put_args.add_argument("userName", type=str,help="Invalid userName", required = True)
student_put_args.add_argument("email", type=str,help="Invalid email",required = True)
student_put_args.add_argument("phone", type=str,help="Invalid phone",required = True)
student_put_args.add_argument("password", type=str,help="Invalid password",required = True)
student_put_args2.add_argument("userName", type=str,help="Invalid userName")
student_put_args2.add_argument("email", type=str,help="Invalid email")
student_put_args2.add_argument("phone", type=str,help="Invalid phone")
student_put_args2.add_argument("password", type=str,help="Invalid password")


resourse_fields = {
    'id':fields.Integer,
    'userName':fields.String,
    'admin':fields.String,
    'email':fields.String,
    'phone':fields.String,
    'password':fields.String,


}
resourse_fields_for_marks = {
'subjectName':fields.String,
    'rating':fields.Integer,
    'studentId':fields.Integer
}
resourse_fields_for_marks2 = {
'rating':fields.Integer
}



def func_for_put(userObject, args):
    if (args["userName"]):
        print('change userName')
        result = Student.query.filter_by(userName=args['userName']).count()
        if (result):
            abort(404, "We already have such a student)")
        userObject.userName = args['userName']
    if (args["email"]):
        print('change email')
        result = Student.query.filter_by(email=args['email']).count()
        if (result):
            abort(404, "We already have such a email)")
        userObject.email = args['email']
    if (args["phone"]):
        print('change phone')
        result = Student.query.filter_by(phone=args['phone']).count()
        if (result):
            abort(404, "We already have such a phone)")
        userObject.phone = args['phone']
    if (args["password"]):
        print('change password')
        userObject.password = generate_password_hash(args['password'])
class Studen(Resource):

    @marshal_with(resourse_fields)
    def post(self, studentName):
        args=student_put_args.parse_args()
        userObject = Student()#userName='', admin=False,email='',phone,)
        func_for_put(userObject, args)
        userObject.admin = False
        db.session.add(userObject)
        db.session.commit()
        userObject = Student.query.filter_by(userName=userObject.userName).first()
        return userObject
    @marshal_with(resourse_fields)
    def get(self,studentName):
        result = Student.query.filter_by(userName=studentName).first()
        if(not result):
            abort(404, "Student not found")
        return result

    @marshal_with(resourse_fields)
    def put(self,studentName):
        args = student_put_args2.parse_args()
        #print(args)
        userObject = Student.query.filter_by(userName=studentName).first()
        if not userObject:
            abort(404, 'Student not found')
        func_for_put(userObject, args)

        db.session.add(userObject)#############################################
        db.session.commit()
        userObject2 = Student.query.filter_by(userName=userObject.userName).first()
        #user = Student(userName="edgfdg", admin=True, email="gfsfg", phone="eadf", password="dsfsdf")
        return userObject2

    def delete(self,studentName):
        userObject = Student.query.filter_by(userName=studentName).first()
        if not userObject:
            abort(404, 'Student not found')
        var1 = True
        while var1:
            markObject = Marks.query.filter_by(studentId=userObject.id).first()
            if not markObject:
                var1 = False
            else:
                db.session.delete(markObject)
                db.session.commit()
        db.session.delete(userObject)
        db.session.commit()
        return HTTPStatus.OK


api.add_resource(Studen, "/student/<string:studentName>")
#app.run()
student_put_args3 = reqparse.RequestParser()
student_put_args4 = reqparse.RequestParser()
student_put_args3.add_argument("studentName", type=str, help="Invalid studentName", required=True)
student_put_args3.add_argument("subjectName", type=str, help="Invalid subjectName", required=True)
student_put_args3.add_argument("mark", type=int, help="Invalid mark", required=True)
student_put_args4.add_argument("studentName", type=str, help="Invalid studentName", required=True)
student_put_args4.add_argument("subjectName", type=str, help="Invalid subjectName", required=True)
#student_put_args5 = reqparse.RequestParser()
#student_put_args5.add_argument("numberOfStudents", type=int, help="Invalid numberOfStudents", required=True)

class StudentMarks(Resource):

    @marshal_with(resourse_fields_for_marks)
    def post(self):

        args=student_put_args3.parse_args()
        if args['mark'] > 12 or args['mark'] < 0:
            abort(404, "The mark must be from 0 to 12 - integer")
        markObject = Marks()
        userObject = Student.query.filter_by(userName=args['studentName']).first()
        #markFromDatabase = Marks.query.filter_by(studentId=userObject.id,subjectName=args['subjectName']).first()
        #if markFromDatabase:
        #    abort(404, "you already have a grade on this subject")
        markObject.studentId = userObject.id
        markObject.subjectName = args['subjectName']
        markObject.rating = args['mark']
        db.session.add(markObject)
        db.session.commit()
        return markObject


    @marshal_with(resourse_fields_for_marks)##########
    def put(self):
        args = student_put_args3.parse_args()
        #print(args)
        userObject = Student.query.filter_by(userName=args['studentName']).first()
        if not userObject:
            abort(404,"Student not found")
        markObject = Marks.query.filter_by(studentId=userObject.id,subjectName=args['subjectName']).first()#, subjectName=args['mark'])
        if not markObject:
            abort(404, "This student does not have such subject(((")
        if args['mark']:
            if 0 > args['mark'] > 12:
                abort(404, "The mark must be from 0 to 12 - integer")
            markObject.rating = args['mark']
        db.session.commit()


        return markObject

    @marshal_with(resourse_fields_for_marks2)  ########
    def get(self):
        args = student_put_args4.parse_args()
        userObject = Student.query.filter_by(userName=args['studentName']).first()
        if not userObject:
            abort(404, "Student not found")
        markObject = Marks.query.filter_by(studentId=userObject.id, subjectName=args['subjectName']).first()
        if not markObject:
            abort(404, "This student does not have such subject((")
        return markObject
    #def delete(self,studentName):
        #userObject = Student.query.filter_by(userName=studentName).first()
        #if not userObject:
        #    abort(404, 'Student not found')
        #db.session.delete(userObject)
        #db.session.commit()
        #return HTTPStatus.OK
api.add_resource(StudentMarks, "/rating")

class StudentStatistics(Resource):


    def get(self,numberOfStudents):
        #args = student_put_args5.parse_args()
        if numberOfStudents <= 0:
            abort(404, "Invalid input")
        result_list = []
        id_of_mark = 1
        var1 = True
        var2 = False
        while var1:
            markObject = Marks.query.filter_by(id=id_of_mark).first()
            if markObject:
                for i in range(len(result_list)):
                    if result_list[i][0] == markObject.studentId:
                        result_list[i][1] += markObject.rating
                        result_list[i][2] += 1
                        var2 = True
                        break
                if not var2:
                    result_list.append([markObject.studentId, markObject.rating, float(1)])
                var2 = False
            id_of_mark += 1
            if (id_of_mark == 1000):
                var1 = False
        for i in range(len(result_list)):
            result_list[i][2] = result_list[i][1]/result_list[i][2]
        result_list = sorted(result_list, key=lambda student: student[2], reverse=True)
        id_of_mark = 0
        result = []
        hash = generate_password_hash("secret password")
        print(hash)
        for i in range(len(result_list)):
            a = Student.query.filter_by(id=result_list[i][0]).first()
            result.append([a.userName, result_list[i][2]])
            id_of_mark += 1
            if(id_of_mark >= numberOfStudents):
                break
        return jsonify(result)
        #markObject = Marks.query.filter_by(studentId=userObject.id, subjectName=args['subjectName']).first()
        #if not markObject:
         #   abort(404, "This student does not have such subject((")
        #return markObject

api.add_resource(StudentStatistics, "/rating/bestStudents/<int:numberOfStudents>")
server = pywsgi.WSGIServer(('127.0.0.1', 5000), app)
server.serve_forever()
#{
#    "userName":"Roman",
#    "email":"dsndbdd33333ff3333353f3333333333333g3333rg",
#    "phone":"sdfgdsdgdfd5ffggdg",
#    "password":"dsfgsgfd5fgdfg"
#}
#{
#    "studentName":"123ddb4d44v4b3",
#    "subjectName":"dsndbddrg",
#    "mark":1
#}