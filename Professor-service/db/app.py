from flask import Flask,request,jsonify
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import func
import datetime


import os
import psycopg2
from dotenv import load_dotenv

app = Flask(__name__)
api = Api(app)

# Load environment variables
load_dotenv()
db_url = os.getenv('DATABASE_URL')

# Connect to database
conn = psycopg2.connect(db_url, sslmode='prefer')

# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Import models
import models.funding, models.professor, models.on_going_research, models.on_going_researches_of_professor, models.on_going_researches_of_student, models.professor_area_of_interests, models.professor_feedback, models.publication, models.university_ranks, models.professor_publications, models.field, models.student_publications, models.funding_fields, models.student_area_of_interests

migrate = Migrate(app, db)