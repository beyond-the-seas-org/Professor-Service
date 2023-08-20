from flask import request,jsonify
from flask_restx import Resource
from professors import db
from professors import api

from professors.models.on_going_research import *

#this class is for adding new on_going_research into database
"""
primary key: id
other fields: research_field, research_topic, description, num_of_students, research_desc_link, funding_id
"""

class Add_on_going_research(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})

    def post(self):

        try:

            #create new on_going_research object
            new_on_going_research = OnGoingResearchModel()
            new_on_going_research.research_field = request.json['research_field']
            new_on_going_research.research_topic = request.json['research_topic']
            new_on_going_research.description = request.json['description']
            new_on_going_research.num_of_students = request.json['num_of_students']
            new_on_going_research.research_desc_link = request.json['research_desc_link']
            new_on_going_research.funding_id = request.json['funding_id']
            
            
            db.session.add(new_on_going_research)
            db.session.commit()

            return jsonify(new_on_going_research.json())
        except Exception as e:
            print({"message":"exception occured in add_on_going_research"})
            print(e)
            return jsonify({"message":"exception occured in add_on_going_research"})
