from flask import request,jsonify
from flask_restx import Resource
from professors import db
from professors import api

from professors.models.university_ranks import *
from professors.models.location import *

#this class is for adding new professor into database

class Add_university_rank(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})

    def post(self):

        try:

            #create new university rank object
            new_university_rank = UniversityRankModel()
            new_university_rank.name = request.json['name']
            new_university_rank.rank = request.json['rank']

            #get the location id from location name
            location_name = request.json['location_name']
            #db must be bind to analytics database
            db.session.bind = 'analytics'
            location_id = LocationModel.query.filter_by(location_name=location_name).first().id

            new_university_rank.location_id = location_id

            #reset the db object binding to the default connection
            db.session.bind = None
            
            db.session.add(new_university_rank)
            db.session.commit()


            return jsonify(new_university_rank.json())
        except Exception as e:
            print({"message":"exception occured in add_university_rank"})
            print(e)
            return jsonify({"message":"exception occured in add_university_rank"})
