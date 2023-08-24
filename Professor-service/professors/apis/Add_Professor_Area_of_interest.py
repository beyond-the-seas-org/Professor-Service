from flask import request,jsonify
from flask_restx import Resource
from professors import db
from professors import api

from professors.models.professor_area_of_interests import *

#this class is for adding new area_of_interest into database
"""
primary key: professor_id and area_of_interest_id
"""

class Add_area_of_interest(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})

    def post(self):

        try:

            #create new area_of_interest object
            new_area_of_interest = ProfessorAreaOfInterestModel()
            new_area_of_interest.professor_id = request.json['professor_id']
            new_area_of_interest.area_of_interest_id = request.json['area_of_interest_id']
            
            db.session.add(new_area_of_interest)
            db.session.commit()

            return jsonify(new_area_of_interest.json())
        except Exception as e:
            print({"message":"exception occured in add_area_of_interest"})
            print(e)
            return jsonify({"message":"exception occured in add_area_of_interest"})
