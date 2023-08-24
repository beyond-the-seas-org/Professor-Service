from flask import request,jsonify
from flask_restx import Resource
from professors import db
from professors import api

from professors.models.professor_website_link import *

#this class is for adding new website into database
"""
primary key: id
other fields: professor_id, website_link, website_type
"""

class Add_website(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})

    def post(self):

        try:

            #create new website object
            new_website = ProfessorWebsiteLinkModel()
            new_website.professor_id = request.json['professor_id']
            new_website.website_link = request.json['website_link']
            new_website.website_type = request.json['website_type']

            db.session.add(new_website)
            db.session.commit()

            return jsonify(new_website.json())
        except Exception as e:
            print({"message":"exception occured in add_website"})
            print(e)
            return jsonify({"message":"exception occured in add_website"})
