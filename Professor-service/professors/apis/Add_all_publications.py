from flask import request,jsonify
from flask_restx import Resource
from professors import db
from professors import api
from datetime import datetime

from professors.models.publication import *

#this class is for adding new publication into database
"""
primary key: id
other fields: title, doi, link, abstract, date, venue, citation, keywords, research_area
"""

class Add_all_publications(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})

    def post(self):

        try:
            all_publication_json = request.json

            for publication_json in all_publication_json:
                publications = publication_json['publications']
                for publication in publications:
                    #checking if the publication already exists
                    publication_exists = PublicationModel.query.filter_by(title=publication['title']).first()
                    if publication_exists:
                        continue
                    new_publication = PublicationModel()
                    new_publication.title = publication['title']
                    new_publication.doi = publication['doi']
                    new_publication.link = publication['link']
                    new_publication.abstract = publication['abstract']

                    if( len(new_publication.abstract) > 10000):
                        new_publication.abstract = new_publication.abstract[:10000]

                    new_publication .citation = None
                    if publication['citations'].isdigit():
                        new_publication.citation = publication['citations']
                    new_publication.venue = 'IEEE'

                    keywords_list = publication['ieee_keywords'] + publication['author_keywords']
                    new_publication.keywords = ', '.join(keywords_list)
                    # print(publication['ieee_keywords'])
                    # print(publication['author_keywords'])

                    new_publication.date = None
                    if(publication['date_of_publication']):

                        date_format = "%d %B %Y"  # Day, full month name, 4-digit year

                        date_obj = datetime.strptime(publication['date_of_publication'], date_format)

                        new_publication.date = date_obj

                    db.session.add(new_publication)
                    db.session.commit()

                    print("Added: ",publication['title'])
                    #return jsonify({"message":"A publication added successfully"})

            return jsonify({"message":"All publications added successfully"})
        except Exception as e:
            print({"message":"exception occured in add_all_publications"})
            print(e)
            return jsonify({"message":"exception occured in add_all_publications"})
