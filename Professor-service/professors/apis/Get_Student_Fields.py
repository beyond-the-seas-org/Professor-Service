from flask import request,jsonify
from flask_restx import Resource
from professors import db
from professors import api

from professors.models.student_area_of_interests import *
from professors.models.field import *

from flask_jwt_extended import jwt_required
from flask_jwt_extended.exceptions import NoAuthorizationError

@api.errorhandler(NoAuthorizationError)
def handle_auth_required(e):
    return {"message": "Authorization token is missing"}, 401

class Get_student_fields(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})
    # @jwt_required()
    def get(self, student_id):

        try:
            #get all field ids of the student
            field_ids = StudentAreaOfInterestModel.query.filter_by(student_id=student_id).with_entities(StudentAreaOfInterestModel.field_id).all()

            #if there are no fields
            if field_ids == []:
                return jsonify({"message":"no fields found"})

            #remove the comma from the tuple
            field_ids = [item for t in field_ids for item in t]


            #get all fields of the student
            fields = FieldModel.query.filter(FieldModel.id.in_(field_ids)).all()

            #convert the fields to json
            fields = [field.json() for field in fields]

            return jsonify(fields)
        
        except Exception as e:
            print({"message":"exception occured in get_students_fields"})
            print(e)
            return jsonify({"message":"exception occured in get_students_fields"})