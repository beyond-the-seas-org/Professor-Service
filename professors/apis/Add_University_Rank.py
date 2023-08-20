from flask import request,jsonify
from flask_restx import Resource
from professors import db
from professors import api

from professors.models.university_ranks import *

#this class is for adding new professor into database

class Add_university_rank(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})

    def post(self):

        try:

            #create new university rank object
            new_university_rank = UniversityRankModel()
            new_university_rank.name = request.json['name']
            new_university_rank.rank = request.json['rank']
            
            db.session.add(new_university_rank)
            db.session.commit()


            return jsonify(new_university_rank.json())
        except Exception as e:
            print({"message":"exception occured in add_university_rank"})
            print(e)
            return jsonify({"message":"exception occured in add_university_rank"})
