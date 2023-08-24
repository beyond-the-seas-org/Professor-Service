from flask import request,jsonify
from flask_restx import Resource
from professors import db
from professors import api

from professors.models.professor_publications import *

#this class is for adding new publication into database
"""
primary key: id
other fields: publication_id, professor_id
"""

class Add_professor_publication(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})

    def post(self):

        try:

            #create new publication object
            new_publication = ProfessorPublicationModel()
            new_publication.publication_id = request.json['publication_id']
            new_publication.professor_id = request.json['professor_id']
            
            db.session.add(new_publication)
            db.session.commit()

            return jsonify(new_publication.json())
        except Exception as e:
            print({"message":"exception occured in add_publication"})
            print(e)
            return jsonify({"message":"exception occured in add_publication"})
