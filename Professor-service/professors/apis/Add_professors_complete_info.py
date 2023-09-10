from flask import request,jsonify
from flask_restx import Resource
from professors import db
from professors import api

from professors.models.professor import * 
from professors.models.university_ranks import *
from professors.models.professor_area_of_interests import *
from professors.models.publication import *
from professors.models.professor_publications import *
from professors.models.field import *

#this class is for adding new professor into database

class Add_professors_complete_info(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})

    def post(self):

        try:
            professors_complete_info = request.json

            for professor_complete_info in professors_complete_info: 
                #getting the university id from university name
                university_name = professor_complete_info['university']
                #checking if the university already exists
                university = UniversityRankModel.query.filter_by(name=university_name).first()
                if university is not None:
                    university_id = university.id
                else:
                    continue
                    


                #Adding a new entry in "professor" table

                #checking if the professor already exists
                professor_exists = ProfessorModel.query.filter_by(name=professor_complete_info['name'],website_link=professor_complete_info['website']).first()
                if professor_exists:
                    continue

                new_professor = ProfessorModel()
                new_professor.name = professor_complete_info['name']
                new_professor.website_link = professor_complete_info['website']
                new_professor.university_id = university_id
                new_professor.image_link = professor_complete_info['image']

                db.session.add(new_professor)
                #print(new_professor.json())

                #Adding a new entries in "professor_area_of_interest" table for each area of interest
                for field_name in professor_complete_info['research_interests']:
                    #finding the field_id from field name
                    

                    field_name = field_name.upper()
                    field_id = FieldModel.query.filter_by(name=field_name).first().id

                    #checking if the professor_area_of_interest already exists
                    professor_area_of_interest_exists = ProfessorAreaOfInterestModel.query.filter_by(professor_id=new_professor.id,area_of_interest_id=field_id).first()
                    if professor_area_of_interest_exists:
                        continue

                    #adding a new entry in "professor_area_of_interest" table
                    new_professor_area_of_interest = ProfessorAreaOfInterestModel()
                    new_professor_area_of_interest.professor_id = new_professor.id
                    new_professor_area_of_interest.area_of_interest_id = field_id

                    db.session.add(new_professor_area_of_interest)
                    #print(new_professor_area_of_interest.json())

                
                #Adding a new entries in "professor_publication" table for each publication
                for publication_link in professor_complete_info['publications']:
                    #finding the publication_id from publication_link

                 
                    publication = PublicationModel.query.filter_by(link=publication_link).first()
                    if publication:
                        new_professor_publication = ProfessorPublicationModel()
                        publication_id = publication.id
                        new_professor_publication.professor_id = new_professor.id
                        new_professor_publication.publication_id = publication.id

                        #checking if the professor_ublication already exists
                        professor_publication_exists = ProfessorPublicationModel.query.filter_by(professor_id=new_professor.id,publication_id=publication_id).first()
                        if professor_publication_exists:
                            continue

                        db.session.add(new_professor_publication)


                db.session.commit()

                print("Added: ",new_professor.name)


            return jsonify({"message":"All professors added successfully"})
        except Exception as e:
            print({"message":"exception occured in add_professor_complete_info"})
            print(e)
            return jsonify({"message":"exception occured in add_professor_complete_info"})
