from flask import request,jsonify
from flask_restx import Resource
from sqlalchemy import func
from itertools import groupby
from professors import db
from professors import api
import pandas as pd
import requests

from professors.models.professor import *
from professors.models.field import *
from professors.models.university_ranks import *
from professors.models.professor_area_of_interests import *
from professors.models.professor_website_link import *

from flask_jwt_extended import jwt_required
from flask_jwt_extended.exceptions import NoAuthorizationError

@api.errorhandler(NoAuthorizationError)
def handle_auth_required(e):
    return {"message": "Authorization token is missing"}, 401


#this class is for getting all shortlisted professors for a student(user_id)

class Get_Shortlisted_Professors_short_details(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})
    @jwt_required()
    def get(self,user_id):


        try:

            #get all shortlisted professors for a student

            response = requests.get(f'http://localhost:5001/api/profile/{user_id}/get_shortlisted_professors')
            response = response.json()
            shortlisted_professors_ids = response['shortlisted_professors_ids']

            
            #get all shortlisted_professors with sorted by university rank
            all_professors_short_details = db.session.query(ProfessorModel, UniversityRankModel).join(UniversityRankModel, ProfessorModel.university_id == UniversityRankModel.id).filter(ProfessorModel.id.in_(shortlisted_professors_ids)).order_by(ProfessorModel.name).all()

            #create json format
            all_professors_short_details_json = []
            for professor in all_professors_short_details:

                #get area of interest ids for each professor
                area_of_interest_ids = db.session.query(ProfessorAreaOfInterestModel.area_of_interest_id).filter(ProfessorAreaOfInterestModel.professor_id == professor[0].id).all()
                #filter the commas from the list
                area_of_interest_ids = [item for t in area_of_interest_ids for item in t]
                # print(area_of_interest_ids)

                #get field names for each area of interest
                
                field_names = db.session.query(FieldModel.name).filter(FieldModel.id.in_(area_of_interest_ids)).all()
                #filter the commas from the list
                field_names = [item for t in field_names for item in t]
                # print(field_names)

                #get website link based on professor id where type = personal
                professor_website_link = db.session.query(ProfessorWebsiteLinkModel.website_link).filter(ProfessorWebsiteLinkModel.professor_id == professor[0].id).filter(ProfessorWebsiteLinkModel.website_type == "personal").first()
                professor_website_link = professor_website_link[0] if professor_website_link else None
                #get the location info from analytics

                
                try:
                    location_id = professor[1].location_id
                    response = requests.get(f'http://localhost:5003/api/analytics/{location_id}/get_location_info')
                    response = response.json()
                    location_name = response['location_name']
                    state_name = response['state_name']
                    country_name = response['country_name']
                    location_info = location_name + ", " + state_name + ", " + country_name
                except Exception as e:
                    print({"message":"exception occured in get_location_info"})
                    print(e)
                    location_info = None

                all_professors_short_details_json.append({
                    "id":professor[0].id,
                    "name":professor[0].name,
                    "email":professor[0].email,
                    "university_id":professor[0].university_id,
                    "university_name":professor[1].name,
                    "university_rank":professor[1].rank,
                    "field_names":field_names,
                    "website_link": professor_website_link,
                    "image_link":professor[0].image_link,
                    "location":location_info
                })
            


            return all_professors_short_details_json
        except Exception as e:
            print({"message":"exception occured in get_shortlisted_professor_short_details"})
            print(e)
            return jsonify({"message":"exception occured in get_shortlisted_professor_short_details"})