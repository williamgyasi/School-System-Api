from flask_restful import Api,Resource,reqparse
from flask import request
from flask_jwt import JWT,jwt_required
students=[{
    "Name":"William Kwabena Gyasi",
    "Age":18,
    "Programme":"General Arts",
    "Parent Details":[
        {
            "Mother Name":"Florence Obinim",
            "Father Name":"John-Agyeman"

        }
    ]
},
{
    "Name":"Johnson Kwabena Gyasi",
    "Age":16,
    "Programme":"Science",
    "Parent Details":[
        {
            "Mother Name":"Yaw Obinim",
            "Father Name":"Peter-Agyeman"

        }
    ]
},
{
    "Name":"Ofori Osei Gyasi",
    "Age":15,
    "Programme":"Social Studies",
    "Parent Details":[
        {
            "Mother Name":"Osei Obayaaa",
            "Father Name":"Osei-Yaw Dwomoh"

        }
    ]
}


]

class Students(Resource):
    @jwt_required()
    def get(self, name, age, programme):
        student = next(filter(lambda x: x["Name"] == name, students), None)
        return (student), 200 if student is not None else 404

    def post(self,name,age,programme):
        if next(filter(lambda x:x['Name']==name,students),None) is not None:
            return {
                "Message":"Student already Exist...."
            },400
        student = {
            "Name": name,
            "Age": age,
            "Programme": programme,
            "Parent Details": [
                {
                    "Mother Name": "Osei Obayaaa",
                    "Father Name": "Osei-Yaw Dwomoh"

                }
            ]

        }
        students.append(student)
        return (students), 201
    def delete(self, name, age, programme):
        global students
        students=list(filter(lambda x:x['Name']!=name,students))
        return {
            'Message':'Student Deleted...'
        }
    def put(self, name, age, programme):
        parser=reqparse.RequestParser()
        parser.add_argument('salary',type=float,required=True,help=("This Field cannot be updated"))
        dataSet=parser.parse_args()
        student=next(filter(lambda x:x["Name"]==name,students),None)
        if student is None:
            student={
                "Name": name,
                "Age": age,
                "Programme": programme,
                "Parent Details": [
                    {
                        "Mother Name": "Osei Obayaaa",
                        "Father Name": "Osei-Yaw Dwomoh"

                    }
                ]
            }
            students.append(student)
            return ({
                "Message":"Student Added Successfully...."
            })
        else:
            student.update(dataSet)
        return student









class StudentList(Resource):
    def get(self):
        return (students),200

