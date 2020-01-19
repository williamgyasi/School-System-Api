from flask import jsonify,request
from flask_restful import Api,Resource
from flask_jwt import JWT,jwt_required
teachers=[{
    "Name":"Mr.Ofori Osei",
    "Course Code":205,
    "Course Name":"English",
    "Salary":5000

}]

class Teachers(Resource):
    @jwt_required()
    def get(self,name,CourseCode,courseName,salary):
       teacher=next(filter(lambda x:x["Name"]==name),None)
       return(teacher),200 if teacher is not None else 404

    def post(self,name,CourseCode,courseName,salary):
        teacher={
            "Name": name,
            "Course Code": CourseCode,
            "Course Name": courseName,
            "Salary": salary}
        teachers.append(teacher)
        return teachers,201
    def delete(self,name,CourseCode,courseName,salary):
        global teachers
        teachers=list(filter(lambda x:x["Name"]!=name,teachers))
        return {
            "Message":"Teacher's Has been deleted"
        }

class TeacherList(Resource):
    def get(self):
        return (teachers),200
