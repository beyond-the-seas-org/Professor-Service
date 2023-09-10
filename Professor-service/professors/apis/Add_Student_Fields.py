from flask import request,jsonify
from flask_restx import Resource
from professors import db
from professors import api

from professors.models.field import *
from professors.models.student_area_of_interests import *

#this class is for adding new field into database
"""
primary key: id
other fields: name
"""

# Assuming that the required field ids and the stundet_id will be sent from frontend
class Add_fields(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})

    def post(self):

        try:
            field_ids = request.json['field_ids']
            student_id = request.json['student_id']

          
            for id in field_ids:
                new_student_field = StudentAreaOfInterestModel()
                new_student_field.field_id = id
                new_student_field.student_id = student_id

                #checking if the field already exists
                field_exists = StudentAreaOfInterestModel.query.filter_by(field_id = id).first()
                if field_exists:
                    continue
                #print("Hello")
         
                db.session.add(new_student_field)
                db.session.commit()

            return jsonify({"message":"all fields added successfully"})
        except Exception as e:
            print({"message":"exception occured in add_student_fields"})
            print(e)
            return jsonify({"message":"exception occured in add_student_fields"})
