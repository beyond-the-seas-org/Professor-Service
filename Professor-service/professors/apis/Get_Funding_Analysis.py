from nltk.tokenize import word_tokenize
from nltk.util import ngrams
from professors import db
from flask import request,jsonify
from flask_restx import Resource
from professors import api

from professors.models.funding import *


# If you haven't downloaded the punkt tokenizer, do so first
# nltk.download('punkt')

class Get_funding_analysis_keywords(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})

    def get(self, funding_id):

        try:
            #get funding requirement details of the funding
            funding_details = FundingModel.query.filter_by(id=funding_id).all()
            funding_details = funding_details[0]
            funding_keywords = extract_keywords(funding_details.requirement_description, cs_terms)
            # print(funding_keywords)


            
            return jsonify(funding_keywords)
        except Exception as e:
            print({"message":"exception occured in get_funding_analysis_keywods"})
            print(e)
            return jsonify({"message":"exception occured in get_funding_analysis_keywods"})


def extract_keywords(text, cs_terms):
    # Tokenize the text
    tokens = word_tokenize(text.lower())

    # Find both one-word and two-word phrases
    one_word_phrases = tokens
    two_word_phrases = [' '.join(gram) for gram in ngrams(tokens, 2)]

    # Combine the one-word and two-word phrases
    all_phrases = one_word_phrases + two_word_phrases

    # Filter out the phrases based on the computer science terms list (case-insensitive)
    keywords = [phrase for phrase in all_phrases if phrase.lower() in cs_terms]

    # Make the list unique
    keywords = list(set(keywords))

    return keywords


# A predefined list of computer science terms (this can be expanded)
cs_terms = {
    "artificial intelligence", "image recognition","neural networks", "optimization", "logistics", 
    "transportation", "finance", "engineering", "machine learning", "data mining", 
    "deep learning", "natural language processing", "algorithm", "computational", 
    "database", "security", "cryptography", "software engineering", "computer graphics", 
    "quantum computing", "distributed systems", "bioinformatics", "robotics", "computer vision",
    "computer architecture", "operating systems", "computer networks", "human-computer interaction",
    "computer science", "computer", "science", "computing", "computers", "software", "hardware"
}

# funding_post = """
# Combinatorial optimization problems are ubiquitous across various industries, ranging from logistics 
# and transportation to finance and engineering. This research project seeks to leverage the capabilities 
# of neural networks to develop novel approaches for solving these intricate problems more efficiently and 
# effectively than traditional methods. By combining the strengths of artificial intelligence and optimization, 
# we aim to push the boundaries of what's possible and create innovative solutions with real-world impact.
# """


