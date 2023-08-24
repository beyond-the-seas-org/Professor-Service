from flask import request,jsonify
from flask_restx import Resource
from professors import db
from professors import api

from professors.models.professor import * 

class Update_professor_image(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})

    def put(self, professor_id):
        try:
            image_link = request.json['image_link']
            professor = ProfessorModel.query.get(professor_id)
            professor.image_link = image_link
            db.session.commit()  # Commit the changes to the database
            return jsonify(professor.json())
        except Exception as e:
            print({"message":"exception occured in Edit_professor_image"})
            print(e)
            return jsonify({"message":"exception occured in Edit_professor_image"})