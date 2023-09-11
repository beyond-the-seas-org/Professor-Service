from flask import request,jsonify
from flask_restx import Resource
from professors import db
from professors import api
from professors.models.funding import *
from professors.models.professor import *
import re # Regular expression operations
import datetime

def extract_funding_details(funding_post):
    # Define regular expressions for different pieces of information
    amount_pattern = r'\$\s?(\d+(?:,\d{3})*(?:\.\d{2})?)'  # Extracts amounts like $10,000.00
    requirement_pattern = r'Requirement:(.*?)(?:Research Overview:|Professor:|$)'  # Extracts requirement description
    slot_pattern = r'(\d+)\s?(?:slots|positions|spots)'  # Extracts numbers of slots
    professor_pattern = r'Professor:\s?(.*?)\s?\n'  # Extracts professor information
    research_pattern = r'Research Overview:\s?(.*?)\s?\n'  # Extracts research overview

    amount_match = re.search(amount_pattern, funding_post)
    requirement_match = re.search(requirement_pattern, funding_post, re.IGNORECASE)
    slot_match = re.search(slot_pattern, funding_post, re.IGNORECASE)
    professor_match = re.search(professor_pattern, funding_post, re.IGNORECASE)
    research_match = re.search(research_pattern, funding_post, re.IGNORECASE)

    # print(requirement_match)

    amount = amount_match.group(1) if amount_match else None
    #convert amount to integer
    amount = int(amount.replace(',', '')) if amount else None
    requirement_description = requirement_match.group(1) if requirement_match else None
    num_of_slots = int(slot_match.group(1)) if slot_match else None
    professor = professor_match.group(1) if professor_match else None
    research_overview = research_match.group(1) if research_match else None

    # print(requirement_description)

    return {
        "amount": amount,
        "requirement_description": requirement_description,
        "num_of_slots": num_of_slots,
        "professor": professor,
        "research_overview": research_overview
    }

#this class is for adding new funding into database
"""
    primary key: id
    other fields: funding_post, date, amount, requirement_description, num_of_slot, professor_id, availability(yes or no)
"""



class Add_funding_from_newsfeed(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})

    def post(self):

        try:

            #retrieve data from request of the newsfeed service
            funding_post = request.json['funding_post']
            extracted_funding_details = extract_funding_details(funding_post)
            professor = extracted_funding_details['professor']
            #check if professor exists in database and get professor id
            professor_obj = ProfessorModel.query.filter(ProfessorModel.name.like(f"%{professor}%")).first()

            if professor_obj:
                professor_id = professor_obj.id

            #create new funding object
            new_funding = FundingModel()
            new_funding.funding_post = extracted_funding_details['research_overview']
            new_funding.date = datetime.datetime.now()
            new_funding.amount = extracted_funding_details['amount']
            new_funding.requirement_description = extracted_funding_details['requirement_description']
            new_funding.num_of_slot = extracted_funding_details['num_of_slots']
            new_funding.professor_id = professor_id
            new_funding.availability = True

            
            db.session.add(new_funding)
            db.session.commit()


            return jsonify(new_funding.json())
        except Exception as e:
            print({"message":"exception occured in add_funding from newsfeed"})
            print(e)
            return jsonify({"message":"exception occured in add_funding from newsfeed"})
