from flask_restx import Resource
from flask import request,jsonify

from professors.models.professor import ProfessorModel
from professors.models.field import FieldModel
from professors.models.university_ranks import UniversityRankModel
from professors.models.professor_area_of_interests import ProfessorAreaOfInterestModel
from professors import api

import requests
import pandas as pd


 #This is an API which will recieve an API request from "Analytic service
 # This API will recieve "fields_of_interest(a list)" from "Professor-Service" and in response from "Professor-service",this API will return a list of "location_id" for those locations in which the professors live who has those area of interest"

class GetLocationsBasedOnFieldOfInterest(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})
    def post(self):

        try:
            fields_of_interest_dict = request.get_json()
            fields_of_interest = fields_of_interest_dict['fields_of_interest']
    
            #retrieving the field_ids for each fields
            fields_of_interest_ids=[]
            all_fields=FieldModel.query.all()
            for field in all_fields:
                if field.name in fields_of_interest:
                    fields_of_interest_ids.append(field.id)

            #retrieving the professors(i.e professor_ids) who have those field of interest
            professor_ids=[]
            all_professors_area_of_interest = ProfessorAreaOfInterestModel.query.all()
            for professor_area_of_interest in all_professors_area_of_interest:
                if professor_area_of_interest.area_of_interest_id in fields_of_interest_ids:
                    professor_ids.append(professor_area_of_interest.professor_id)

            #"professor_ids" list can have repeated values(i.e. professor_id can be repeated in the list).thats why the following line
            # makes the "professor_ids" list as the list of unique professor_ids
            professor_ids = list(set(professor_ids)) 


            #Now we will find the "university_ids" where the above filtered professors are appointed
            university_ids=[]
            all_professors = ProfessorModel.query.all()
            for professor in all_professors:
                if professor.id in professor_ids:
                    university_ids.append(professor.university_id)

            #"university_ids" list can have repeated values.thats why the following line makes the "university_ids" line with unique values
            university_ids = list(set(university_ids)) 

            
            #Now finally,we will find the list of locations where those universities are (i.e. those professors live)
            location_ids = []
            all_universities = UniversityRankModel.query.all()
            for university in all_universities:
                if university.id in university_ids:
                    location_ids.append(university.location_id)

            location_ids = list(set(location_ids)) 

            return jsonify({"location_ids":location_ids})
        
        except Exception as e:
            print({"message":"exception occured in get_location_based_on_field_of_interest"})
            print(e)
            return jsonify({"message":"exception occured in get_location_based_on_field_of_interest"})      



        