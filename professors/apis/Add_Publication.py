from flask import request,jsonify
from flask_restx import Resource
from professors import db
from professors import api

from professors.models.publication import *

#this class is for adding new publication into database
"""
primary key: id
other fields: title, doi, link, abstract, date, venue, citation, keywords, research_area
"""

class Add_publication(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})

    def post(self):

        try:

            #create new publication object
            new_publication = PublicationModel()
            new_publication.title = request.json['title']
            new_publication.doi = request.json['doi']
            new_publication.link = request.json['link']
            new_publication.abstract = request.json['abstract']
            new_publication.date = request.json['date']
            new_publication.venue = request.json['venue']
            new_publication.citation = request.json['citation']
            new_publication.keywords = request.json['keywords']
            new_publication.research_area = request.json['research_area']
            
            db.session.add(new_publication)
            db.session.commit()


            return jsonify(new_publication.json())
        except Exception as e:
            print({"message":"exception occured in add_publication"})
            print(e)
            return jsonify({"message":"exception occured in add_publication"})
