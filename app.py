from flask import Flask,request,jsonify
import StudentResources as  Rs
import TeacherResources as Ts
from flask_restful import Api,Resource
from flask_jwt import JWT
from security import authenticate,identity





app=Flask(__name__)
app.secret_key="404 not found"
api=Api(app)
#JWT TOKEN REQUEST
jwt=JWT(app,authenticate,identity)

#Resource Handling for Student Requests

api.add_resource(Rs.Students,'/student/<string:name>/<string:age>/<string:programme>')
api.add_resource(Ts.Teachers,'/teacher/<string:name>/<string:CourseCode>/<string:courseName>/<string:salary>')
api.add_resource(Rs.StudentList,'/students')
api.add_resource(Ts.TeacherList,'/teachers')


if __name__=="__main__":
    app.run(debug=True)
