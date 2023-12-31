from flask import request,jsonify
from flask_restx import Resource
from professors import db
from professors import api

from professors.models.professor import * 
from professors.models.university_ranks import *

#this class is for adding new professor into database

class Add_professor(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})

    def post(self):

        try:

            #get the university id from university name
            university_name = request.json['university_name']
            university_id = UniversityRankModel.query.filter_by(name=university_name).first().id
            print(university_id)

            #create new professor object
            new_professor = ProfessorModel()
            new_professor.name = request.json['name']
            new_professor.email = request.json['email']
            new_professor.university_id = university_id
            new_professor.location_id = request.json['location_id']
            new_professor.image_link = request.json['image_link']

            db.session.add(new_professor)
            db.session.commit()


            return jsonify(new_professor.json())
        except Exception as e:
            print({"message":"exception occured in add_professor"})
            print(e)
            return jsonify({"message":"exception occured in add_professor"})
