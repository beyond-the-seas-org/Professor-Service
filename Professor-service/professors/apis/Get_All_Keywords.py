from flask_restx import Resource
from flask import request,jsonify
from professors import api
import requests

from professors.models.publication import PublicationModel


 #This is an API which will recieve an API "GET" request from "Analytic service"
 # This API will return all keywords to "Analytic service" 

class Get_All_Keywords(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})
    def get(self):

        try:
            all_keywords = [publication.keywords for publication in PublicationModel.query.all()]
            all_keywords = [keyword.split(",") for keyword in all_keywords]
            # split keywords into list of keywords
            all_keywords = [keyword for keywords in all_keywords for keyword in keywords]
            #remove any starting space from keywords
            all_keywords = [keyword.strip() for keyword in all_keywords]
            # split keywords in respect of comma and create a set of keywords
            all_keywords = list(set(all_keywords))
            return jsonify({"keywords":all_keywords})  
        
        except Exception as e:
            print({"message":"exception occured in get_all_keywords"})
            print(e)
            return jsonify({"message":"exception occured in get all keywords"})      



             


 


       