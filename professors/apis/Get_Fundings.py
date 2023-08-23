from flask import request,jsonify
from flask_restx import Resource
from sqlalchemy import func
from itertools import groupby
from professors import db
from professors import api
import pandas as pd
import requests

from professors.models.professor import *
from professors.models.funding import *
from professors.models.funding_fields import *
from professors.models.field import *

#this class is for getting all professors from database

class Get_fundings(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})

    def get(self):

        try:
            #get all professors with sorted by university rank
            all_fundings = db.session.query(FundingModel, ProfessorModel).join(FundingModel, ProfessorModel.id == FundingModel.professor_id).order_by(FundingModel.date).all()

            #get the field names from funding_fields and field table for each funding_id
            for funding in all_fundings:
                funding_fields = FundingFieldsModel.query.filter_by(funding_id=funding[0].id).all()
                field_names = []
                for funding_field in funding_fields:
                    field = FieldModel.query.filter_by(id=funding_field.field_id).first()
                    field_names.append(field.name)
                funding[0].field_names = field_names



        

            #create json format
            all_fundings_json = []
            #funding_post, date, amount, requirement_description, num_of_slot, professor.name
            for funding in all_fundings:
                all_fundings_json.append({
                    "id":funding[0].id,
                    "funding_post":funding[0].funding_post,
                    "date":funding[0].date,
                    "amount":funding[0].amount,
                    "requirement_description": funding[0].requirement_description,
                    "num_of_slot": funding[0].num_of_slot,
                    "professor_name": funding[1].name,
                    "location": funding[1].location,
                    "availability": funding[0].availability,
                    "field_names": funding[0].field_names,
                    "professor_image": funding[1].image_link
                })
            return jsonify(all_fundings_json)
        except Exception as e:
            print({"message":"exception occured in get_fundings"})
            print(e)
            return jsonify({"message":"exception occured in get_fundings"})
        