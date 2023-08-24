from flask import request,jsonify
from flask_restx import Resource
from professors import db
from professors import api

from professors.models.student_publications import *
from professors.models.publication import *

class Get_students_research_keywords(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})

    def get(self, student_id):

        try:
            #get all publication ids of the student
            publication_ids = db.session.query(StudentPublicationModel.publication_id).filter(StudentPublicationModel.student_id == student_id).all()
            #filter the commas from the list
            publication_ids = [item for t in publication_ids for item in t]

            #get all publication keywords of the student
            publication_keywords = db.session.query(PublicationModel.keywords).filter(PublicationModel.id.in_(publication_ids)).all()
            #filter the commas from the list
            publication_keywords = [item for t in publication_keywords for item in t]

            #json format
            publication_keywords_json = []
            for keyword in publication_keywords:
                publication_keywords_json.append({
                    "keyword":keyword
                })

            return jsonify(publication_keywords_json)
        except Exception as e:
            print({"message":"exception occured in get_students_research_keywords"})
            print(e)
            return jsonify({"message":"exception occured in get_students_research_keywords"})