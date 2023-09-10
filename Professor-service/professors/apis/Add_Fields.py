from flask import request,jsonify
from flask_restx import Resource
from professors import db
from professors import api

from professors.models.field import *

#this class is for adding new field into database
"""
primary key: id
other fields: name
"""
class Add_fields(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})

    def post(self):

        try:
            fields = request.json['fields']

            print("total fields: ",len(fields))
          
            for field in fields:
                new_field = FieldModel()
                new_field.name = field

                #checking if the field already exists
                field_exists = FieldModel.query.filter_by(name=field).first()
                if field_exists:
                    continue
                #print("Hello")
         
                db.session.add(new_field)
                db.session.commit()
                print("Adding ",field)

            return jsonify({"message":"all fields added successfully"})
        except Exception as e:
            print({"message":"exception occured in add_fields"})
            print(e)
            return jsonify({"message":"exception occured in add_fields"})
