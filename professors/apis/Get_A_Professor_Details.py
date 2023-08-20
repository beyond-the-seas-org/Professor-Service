from flask import request,jsonify
from flask_restx import Resource
from sqlalchemy import func
from itertools import groupby
from professors import db
from professors import api
import pandas as pd
import requests

from professors.models.professor import *
from professors.models.university_ranks import *
from professors.models.publication import *
from professors.models.professor_publications import *
from professors.models.on_going_research import *
from professors.models.on_going_researches_of_professor import *
from professors.models.professor_area_of_interests import *
from professors.models.funding import *
from professors.models.professor_feedback import *
from professors.models.professor_website_link import *
from professors.models.field import *

class Get_a_professor_details(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})

    def get(self, professor_id):

        try:
            professor_details = ProfessorModel.query.filter_by(id=professor_id).all()
            university_details = UniversityRankModel.query.filter_by(id=professor_details[0].university_id).all()

            area_of_interest_ids = db.session.query(ProfessorAreaOfInterestModel.area_of_interest_id).filter(ProfessorAreaOfInterestModel.professor_id == professor_id).all()
            area_of_interest_ids = [interest_id for (interest_id,) in area_of_interest_ids]

            field_names = db.session.query(FieldModel.name).filter(FieldModel.id.in_(area_of_interest_ids)).all()
            field_names = [name for (name,) in field_names]

            publication_ids = db.session.query(ProfessorPublicationModel.publication_id).filter(ProfessorPublicationModel.professor_id == professor_id).all()
            publication_ids = [publication_id for (publication_id,) in publication_ids]
            
            publication_details = []
            for publication_id in publication_ids:
                publication = PublicationModel.query.filter_by(id=publication_id).all()
                #make json format: fields: title, doi, link, abstract, date, venue, citation, keywords, research_area
                publication_details.append({
                    "title":publication[0].title,
                    "doi":publication[0].doi,
                    "link":publication[0].link,
                    "abstract":publication[0].abstract,
                    "date":publication[0].date.isoformat(),
                    "venue":publication[0].venue,
                    "citation":publication[0].citation,
                    "keywords":publication[0].keywords,
                    "research_area":publication[0].research_area
                })


            on_going_research_ids = db.session.query(OnGoingResearchOfProfessorModel.on_going_research_id).filter(OnGoingResearchOfProfessorModel.professor_id == professor_id).all()
            on_going_research_ids = [research_id for (research_id,) in on_going_research_ids]

            on_going_research_details = []
            #research_field, research_topic, description, num_of_students, research_desc_link, funding_id
            for on_going_research_id in on_going_research_ids:
                research = OnGoingResearchModel.query.filter_by(id=on_going_research_id).all()
                funding = FundingModel.query.filter_by(id=research[0].funding_id).all()
                on_going_research_details.append({
                    "research_field":research[0].research_field,
                    "research_topic":research[0].research_topic,
                    "description":research[0].description,
                    "num_of_students":research[0].num_of_students,
                    "research_desc_link":research[0].research_desc_link,
                    "funding":funding[0].id
                })



            funding_details = FundingModel.query.filter_by(professor_id=professor_id).all()

            funding_details_json = []
            #fields: funding_post, date, amount, requirement_description, num_of_slot, professor_id, availability
            for funding in funding_details:
                funding_details_json.append({
                    "funding_post":funding.funding_post,
                    "date":funding.date.isoformat(),
                    "amount":funding.amount,
                    "requirement_description":funding.requirement_description,
                    "num_of_slot":funding.num_of_slot,
                    "professor_id":funding.professor_id,
                    "availability":funding.availability
                })


            professor_feedback_details = ProfessorFeedbackModel.query.filter_by(professor_id=professor_id).all()
            
            professor_feedback_details_json = []
            #professor_id, profile_id, feedback
            for feedback in professor_feedback_details:
                professor_feedback_details_json.append({
                    "professor_id":feedback.professor_id,
                    "profile_id":feedback.profile_id,
                    "feedback":feedback.feedback
                })
            professor_website_link_details = ProfessorWebsiteLinkModel.query.filter_by(professor_id=professor_id).all()

            professor_website_link_details_json = []
            #website_link, website_type
            for website_link in professor_website_link_details:
                professor_website_link_details_json.append({
                    "website_link":website_link.website_link,
                    "website_type":website_link.website_type
                })

            
            #create json format
            professor_details_json = []
            professor_details_json.append({
                "id":professor_details[0].id,
                "name":professor_details[0].name,
                "email":professor_details[0].email,
                "university_id":professor_details[0].university_id,
                "university_name":university_details[0].name,
                "university_rank":university_details[0].rank,
                "field_names":field_names,
                "publications":publication_details,
                "on_going_researches":on_going_research_details,
                "funding":funding_details_json,
                "feedback":professor_feedback_details_json,
                "website_link":professor_website_link_details_json
            })

            return professor_details_json
        except Exception as e:
            print({"message":"exception occured in get_a_professor_details"})
            print(e)
            return jsonify({"message":"exception occured in get_a_professor_details"})


