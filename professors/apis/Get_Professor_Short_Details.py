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

#this class is for getting all professors from database

class Get_All_professor_short_details(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})

    def get(self):

        try:
            #get all professors
            all_professors_short_details = db.session.query(ProfessorModel, UniversityRankModel).filter(ProfessorModel.university_id == UniversityRankModel.id).all()

            print(all_professors_short_details)

            #create json format
            all_professors_short_details_json = []
            for professor in all_professors_short_details:
                all_professors_short_details_json.append({
                    "id":professor[0].id,
                    "name":professor[0].name,
                    "university_id":professor[0].university_id,
                    "university_name":professor[1].name,
                    "university_rank":professor[1].rank
                })
            


            return all_professors_short_details_json
        except Exception as e:
            print({"message":"exception occured in get_all_professor_short_details"})
            print(e)
            return jsonify({"message":"exception occured in get_all_professor_short_details"})