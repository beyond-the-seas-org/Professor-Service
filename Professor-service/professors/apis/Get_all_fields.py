from flask_restx import Resource
from flask import request,jsonify
from professors import api
import requests

from professors.models.field import FieldModel


 #This is an API which will recieve an API "GET" request from "Analytic service"
 # This API will return all fields to "Analytic service" 

class Get_all_fields(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})
    def get(self):

        try:
            all_fields = [field.name for field in FieldModel.query.order_by(FieldModel.name.asc()).all()]  
            return jsonify({"fields":all_fields})  
        
        except Exception as e:
            print({"message":"exception occured in get_all_fields"})
            print(e)
            return jsonify({"message":"exception occured in get_location_based_on_field_of_interest"})      



             


 


       