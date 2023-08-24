from flask import request,jsonify
from flask_restx import Resource
from professors import db
from professors import api

from professors.models.on_going_researches_of_professor import *

#this class is for adding new on_going_research of professor into database
"""
primary key: professor_id and on_going_research_id
"""

class Add_on_going_research_professor(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})

    def post(self):

        try:

            #create new on_going_research object
            new_on_going_research_professor = OnGoingResearchOfProfessorModel()
            new_on_going_research_professor.professor_id = request.json['professor_id']
            new_on_going_research_professor.on_going_research_id = request.json['on_going_research_id']
            
            
            db.session.add(new_on_going_research_professor)
            db.session.commit()

            return jsonify(new_on_going_research_professor.json())
        except Exception as e:
            print({"message":"exception occured in add_on_going_research_professor"})
            print(e)
            return jsonify({"message":"exception occured in add_on_going_research_professor"})
