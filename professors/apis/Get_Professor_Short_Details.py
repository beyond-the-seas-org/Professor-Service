from flask import request,jsonify
from flask_restx import Resource
from sqlalchemy import func
from itertools import groupby
from professors import db
from professors import api
import pandas as pd
import requests

from professors.models.professor import *
from professors.models.field import *

#this class is for getting all professors from database

class Get_All_professor_short_details(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})

    def get(self):

        try:
            #get all professors
            all_professors_short_details = ProfessorModel.query.all()
            #all_posts = db.session.query(StudentModel,PostModel,CommentModel,aliased_Student_model).filter(StudentModel.id == PostModel.profile_id).filter(CommentModel.post_id == PostModel.id).filter(CommentModel.profile_id == aliased_Student_model.id).order_by(PostModel.date.desc()).all()
            
            #get all fields
            all_fields = FieldModel.query.all()

            return jsonify(all_professors.json())
        except Exception as e:
            print({"message":"exception occured in get_all_professor_short_details"})
            print(e)
            return jsonify({"message":"exception occured in get_all_professor_short_details"})