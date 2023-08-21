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

#this class is for getting all professors from database

class Get_All_professor_short_details(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})

    def get(self):

        try:
            #get all professors with sorted by university rank
            all_professors_short_details = db.session.query(ProfessorModel, UniversityRankModel).join(UniversityRankModel, ProfessorModel.university_id == UniversityRankModel.id).order_by(ProfessorModel.name).all()
            

            print(all_professors_short_details)



            

            #create json format
            all_professors_short_details_json = []
            for professor in all_professors_short_details:

                #get area of interest ids for each professor
                area_of_interest_ids = db.session.query(ProfessorAreaOfInterestModel.area_of_interest_id).filter(ProfessorAreaOfInterestModel.professor_id == professor[0].id).all()
                #filter the commas from the list
                area_of_interest_ids = [item for t in area_of_interest_ids for item in t]
                print(area_of_interest_ids)

                #get field names for each area of interest
                
                field_names = db.session.query(FieldModel.name).filter(FieldModel.id.in_(area_of_interest_ids)).all()
                #filter the commas from the list
                field_names = [item for t in field_names for item in t]
                print(field_names)

                #get website links for each professor
                website_links = db.session.query(ProfessorWebsiteLinkModel.id).filter(ProfessorWebsiteLinkModel.professor_id == professor[0].id).all()
                #filter the commas from the list
                website_links = [item for t in website_links for item in t]

                all_professors_short_details_json.append({
                    "id":professor[0].id,
                    "name":professor[0].name,
                    "email":professor[0].email,
                    "university_id":professor[0].university_id,
                    "university_name":professor[1].name,
                    "university_rank":professor[1].rank,
                    "field_names":field_names,
                    "website_links":website_links
                })
            


            return all_professors_short_details_json
        except Exception as e:
            print({"message":"exception occured in get_all_professor_short_details"})
            print(e)
            return jsonify({"message":"exception occured in get_all_professor_short_details"})