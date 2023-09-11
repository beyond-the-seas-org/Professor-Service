from flask import request,jsonify
from flask_restx import Resource
from professors import db
from professors import api
import requests

from nltk.tokenize import word_tokenize
from nltk.util import ngrams
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from flask_jwt_extended import jwt_required
from flask_jwt_extended.exceptions import NoAuthorizationError

@api.errorhandler(NoAuthorizationError)
def handle_auth_required(e):
    return {"message": "Authorization token is missing"}, 401


def jaccard_similarity(set1, set2):
    intersection = len(set1.intersection(set2))
    similarity = intersection / len(set2) * 100 if len(set2) != 0 else 0
    return similarity


def match_my_research_area(funding_keywords, student_keywords):
    funding_set = set(funding_keywords.replace(" ", "").lower().split(","))
    student_set = set(student_keywords.replace(" ", "").lower().split(","))
    print("funding_set", funding_set)
    print("student_set", student_set)
    similarity_score = jaccard_similarity(student_set, funding_set)
    matched_keywords = list(funding_set.intersection(student_set))
    print(matched_keywords)
    return similarity_score, matched_keywords

# def calculate_cosine_similarity(keyword_set1, keyword_set2):
#     tfidf_vectorizer = TfidfVectorizer()
#     tfidf_matrix = tfidf_vectorizer.fit_transform([keyword_set1, keyword_set2])
#     cosine_sim = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])
#     return cosine_sim[0][0]

# def match_my_research_area(funding_keywords, student_keywords):
#     cosine_similarity_score = calculate_cosine_similarity(funding_keywords, student_keywords)
#     similarity_percentage = cosine_similarity_score * 100
#     return similarity_percentage

class Get_student_profile_matching(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})
    @jwt_required()
    def get(self, student_id, funding_id):
        try:
            funding_keywords = requests.get(f'http://127.0.0.1:5002/api/professors/{funding_id}/get_funding_analysis_keywords')

            student_keywords = requests.get(f'http://127.0.0.1:5002/api/professors/{student_id}/get_students_research_keywords')
            # print(student_keywords.json())
            # print(funding_keywords.json())
            #make all the student keywords into a list
            student_keywords = [keyword['keyword'] for keyword in student_keywords.json()]
            # #iterate student_keywords and replace ' with space

            # output the list of keywords in a comma separated string
            student_keywords = ", ".join(student_keywords)

            funding_keywords = funding_keywords.json()

            #make all the funding keywords in a comma separated string
            funding_keywords = ", ".join(funding_keywords)            

            similarity, matched_keywords = match_my_research_area(funding_keywords, student_keywords)

            return jsonify({"similarity":similarity, "matched_keywords":matched_keywords})
        except Exception as e:
            print({"message":"exception occured in get_student_profile_matching"})
            print(e)
            return jsonify({"message":"exception occured in get_student_profile_matching"})
    

        