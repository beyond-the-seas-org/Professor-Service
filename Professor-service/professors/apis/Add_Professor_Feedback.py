from flask import request,jsonify
from flask_restx import Resource
from professors import db
from professors import api

from professors.models.professor_feedback import *

#this class is for adding new feedback into database
"""
primary key: id
other fields: professor_id, profile_id, feedback
"""

class Add_feedback(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})

    def post(self):

        try:

            #create new feedback object
            new_feedback = ProfessorFeedbackModel()
            new_feedback.professor_id = request.json['professor_id']    
            new_feedback.profile_id = request.json['profile_id']
            new_feedback.feedback = request.json['feedback']
            
            db.session.add(new_feedback)
            db.session.commit()

            return jsonify(new_feedback.json())
        except Exception as e:
            print({"message":"exception occured in add_feedback"})
            print(e)
            return jsonify({"message":"exception occured in add_feedback"})
