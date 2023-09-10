from flask import request,jsonify
from flask_restx import Resource
from professors import db
from professors import api
import datetime
import json

from professors.models.student_publications import *
from professors.models.publication import *

#this class is for adding new publication into database and then adding the publication id and student id into student_publications table. The input will be publication details in json format and student id
""" 
primary key: id
other fields: publication_id, student_id
"""

class Add_student_publication(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})

    def post(self):

        try:
            publication_exists = PublicationModel.query.filter_by(title=request.json['title']).first()
            if publication_exists:
                #update the publication date if it is not present
                if not publication_exists.date:
                    publication_exists.date = request.json['date_of_publication']
                
                # update citations
                publication_exists.citation = None
                if request.json['citations'].isdigit():
                    publication_exists.citation = request.json['citations']
                
                db.session.commit()
                


                # then add the publication id and student id into student_publications table
                new_student_publication = StudentPublicationModel()
                new_student_publication.publication_id = publication_exists.id
                new_student_publication.student_id = request.json['student_id']

                #check if the student publication already exists
                student_publication_exists = StudentPublicationModel.query.filter_by(publication_id = publication_exists.id, student_id = request.json['student_id']).first()
                if student_publication_exists:
                    return jsonify(student_publication_exists.json())
                
                db.session.add(new_student_publication)
                db.session.commit()

                return jsonify(publication_exists.json())

            new_publication = PublicationModel()
            new_publication.title = request.json['title']
            new_publication.doi = request.json['doi']
            new_publication.abstract = request.json['abstract']
            if( len(new_publication.abstract) > 10000):
                new_publication.abstract = new_publication.abstract[:10000]
            
            new_publication.link = request.json['link']
            new_publication.date = None
            if(request.json['date_of_publication']):
                # check if the date_of_publication is of type Date, then convert it to datetime object
                if type(request.json['date_of_publication']) is datetime.date:
                    new_publication.date = request.json['date_of_publication']
                else:
                    date_format = "%d %B %Y"  # Day, full month name, 4-digit year
                    date_obj = datetime.strptime(request.json['date_of_publication'], date_format)
                    new_publication.date = date_obj

            new_publication.venue = request.json['venue']
            new_publication.citation = None
            if request.json['citations'].isdigit():
                new_publication.citation = request.json['citations']

            new_publication.keywords = request.json['keywords']
            
            db.session.add(new_publication)
            db.session.commit()

            #get the id of the newly created publication
            publication_id = new_publication.id
            new_student_publication = StudentPublicationModel()
            new_student_publication.publication_id = publication_id
            new_student_publication.student_id = request.json['student_id']

            db.session.add(new_student_publication)
            db.session.commit()

            return jsonify(new_publication.json())
        except Exception as e:
            print({"message":"exception occured in add_student_publication"})
            print(e)
            return jsonify({"message":"exception occured in add_student_publication"})
