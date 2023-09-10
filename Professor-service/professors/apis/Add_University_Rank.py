from flask import request,jsonify
from flask_restx import Resource
from professors import db
from professors import api
import requests

from professors.models.university_ranks import *

#this class is for adding new professor into database

class Add_university_rank(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})

    def post(self):

        try:

            universities = request.json
            for university in universities:
                #checking if the university already exists
                university_exists = UniversityRankModel.query.filter_by(name=university['name']).first()
                if university_exists:
                    continue
                
                #create new university rank object
                new_university_rank = UniversityRankModel()
                new_university_rank.name = university['name']
                new_university_rank.rank = university['rank']
                location = university['location']
                if(location == "Location not found"):
                    continue

                location_attributes = location.split(",")
                location_name = location_attributes[0]
                state_name = location_attributes[1].lstrip()
                country_name = location_attributes[len(location_attributes)-1].lstrip()
                location = {
                    "location_name": location_name,
                    "state_name": state_name,
                    "country_name": country_name
                }
                response = requests.post("http://localhost:5003/api/analytics/get_location_id", json=location)
                location_id = response.json()['location_id']
                new_university_rank.location_id = location_id
                
                db.session.add(new_university_rank)
                db.session.commit()


            return jsonify({"message":"All universities added successfully"})
        except Exception as e:
            print({"message":"exception occured in add_university_rank"})
            print(e)
            return jsonify({"message":"exception occured in add_university_rank"})
