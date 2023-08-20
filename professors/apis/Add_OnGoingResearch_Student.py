from flask import request,jsonify
from flask_restx import Resource
from professors import db
from professors import api

from professors.models.on_going_researches_of_student import *

#this class is for adding new on_going_research of student into database
"""
primary key: profile_id and on_going_research_id
"""
class Add_on_going_research_student(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})

    def post(self):

        try:

            #create new on_going_research object
            new_on_going_research_student = OnGoingResearchOfStudentModel()
            new_on_going_research_student.profile_id = request.json['profile_id']
            new_on_going_research_student.on_going_research_id = request.json['on_going_research_id']
            
            
            db.session.add(new_on_going_research_student)
            db.session.commit()

            return jsonify(new_on_going_research_student.json())
        except Exception as e:
            print({"message":"exception occured in add_on_going_research_student"})
            print(e)
            return jsonify({"message":"exception occured in add_on_going_research_student"})
