from flask import request,jsonify
from flask_restx import Resource
from professors import db
from professors import api

from professors.models.funding import *

#this class is for adding new funding into database
"""
    primary key: id
    other fields: funding_post, date, amount, requirement_description, num_of_slot, professor_id, availability(yes or no)
"""

class Add_funding(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})

    def post(self):

        try:

            #create new funding object
            new_funding = FundingModel()
            new_funding.funding_post = request.json['funding_post']
            new_funding.date = request.json['date']
            new_funding.amount = request.json['amount']
            new_funding.requirement_description = request.json['requirement_description']
            new_funding.num_of_slot = request.json['num_of_slot']
            new_funding.professor_id = request.json['professor_id']
            new_funding.availability = request.json['availability']

            
            db.session.add(new_funding)
            db.session.commit()


            return jsonify(new_funding.json())
        except Exception as e:
            print({"message":"exception occured in add_funding"})
            print(e)
            return jsonify({"message":"exception occured in add_funding"})
