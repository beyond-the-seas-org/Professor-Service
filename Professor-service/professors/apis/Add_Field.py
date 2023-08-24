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
class Add_field(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})

    def post(self):

        try:

            #create new field object
            new_field = FieldModel()
            new_field.name = request.json['name']
            
            db.session.add(new_field)
            db.session.commit()

            return jsonify(new_field.json())
        except Exception as e:
            print({"message":"exception occured in add_field"})
            print(e)
            return jsonify({"message":"exception occured in add_field"})
