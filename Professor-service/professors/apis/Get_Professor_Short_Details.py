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

#this class is for getting all professors from database

from flask_jwt_extended import jwt_required
from flask_jwt_extended.exceptions import NoAuthorizationError

@api.errorhandler(NoAuthorizationError)
def handle_auth_required(e):
    return {"message": "Authorization token is missing"}, 401

class Get_All_professor_short_details(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})
    @jwt_required()
    def get(self,user_id):
        # print("inside get_all_professor_short_details")

        try:
            
            #at first the shortlisted professors ids are retrieved for this student because we need to show the shortlist status for each professor.Upon on this "shortlist status" for each professor it will be decided that "Add to shortlist" button will be shown or "Remove from shortlist" button will be shown for each professor in the frontend
            token = request.headers.get('Authorization')
            if token and token.startswith('Bearer '):
                access_token = token.split(' ')[1]

            try:
                response = requests.get(f'http://127.0.0.1:5001/api/profile/{user_id}/get_shortlisted_professors')
                response = response.json()
                shortlisted_professors_ids = response['shortlisted_professors_ids']

               
                

            except Exception as e:
                #print({"message":"exception occured in get_shortlisted_professors"})
                print(e)
                shortlisted_status = False

            page = int(request.args.get('page', 1))  # Get the page parameter (default to 1)
            page_size = int(request.args.get('pageSize', 20))  # Get the pageSize parameter (default to 20)
            start_index = (page - 1) * page_size 
            end_index = page * page_size

            #get professors from id start_index to end_index with sorted by university rank
            all_professors_short_details = db.session.query(ProfessorModel, UniversityRankModel).join(UniversityRankModel, ProfessorModel.university_id == UniversityRankModel.id).order_by(ProfessorModel.name).slice(start_index, end_index).all()

            #get all professors with sorted by university rank
            # all_professors_short_details = db.session.query(ProfessorModel, UniversityRankModel).join(UniversityRankModel, ProfessorModel.university_id == UniversityRankModel.id).order_by(ProfessorModel.name).all()

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
                # professor_website_link = db.session.query(ProfessorWebsiteLinkModel.website_link).filter(ProfessorWebsiteLinkModel.professor_id == professor[0].id).filter(ProfessorWebsiteLinkModel.website_type == "personal").first()
                # professor_website_link = professor_website_link[0] if professor_website_link else None

                #setting shortlist_status for this professor of this student
                shortlist_status = False
                if professor[0].id in shortlisted_professors_ids:
                    shortlist_status = True
               
                #get the location info from analytics
                try:
                    location_id = professor[1].location_id
                    response = requests.get(f'http://127.0.0.1:5003/api/analytics/{location_id}/get_location_info',
                                            headers={'Authorization': f'Bearer {access_token}'})
                    if response.status_code == 401:
                        return {"message":"Invalid token"}, 401
                    response = response.json()
                    location_name = response['location_name']
                    state_name = response['state_name']
                    country_name = response['country_name']
                    location_info = location_name + ", " + state_name + ", " + country_name
                except Exception as e:
                    #print({"message":"exception occured in get_location_info"})
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
                    "website_link": professor[0].website_link,
                    "image_link":professor[0].image_link,
                    "location":location_info,
                    "shortlist_status":shortlist_status

                })
            


            return all_professors_short_details_json
        except Exception as e:
            print({"message":"exception occured in get_all_professor_short_details"})
            print(e)
            return jsonify({"message":"exception occured in get_all_professor_short_details"})