from flask import request,jsonify
from flask_restx import Resource
from professors import db
from professors import api

from professors.models.student_publications import *
from professors.models.publication import *

class Get_student_publications(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})

    def get(self, student_id):

        try:
            #get all publication ids of the student
            publication_ids = StudentPublicationModel.query.filter_by(student_id=student_id).with_entities(StudentPublicationModel.publication_id).all()

            #if there are no publications
            if publication_ids == []:
                return jsonify({"message":"no publications found"})

            #remove the comma from the tuple
            publication_ids = [item for t in publication_ids for item in t]


            #get all publications of the student
            publications = PublicationModel.query.filter(PublicationModel.id.in_(publication_ids)).all()

            #convert the publications to json
            publications = [publication.json() for publication in publications]

            return jsonify(publications)
        except Exception as e:
            print({"message":"exception occured in get_students_publications"})
            print(e)
            return jsonify({"message":"exception occured in get_students_publications"})