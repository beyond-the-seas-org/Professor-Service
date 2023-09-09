from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import psycopg2, dotenv, os
from flask_restx import Api
from flask_cors import CORS
from flask_jwt_extended import JWTManager

app = Flask(__name__)
api = Api(app)
CORS(app,origins = 'http://127.0.0.1:3000')


dotenv.load_dotenv()
db_url = os.getenv('DATABASE_URL')

conn = psycopg2.connect(db_url, sslmode='prefer')

# app.config['SQLALCHEMY_DATABASE_URI'] = db_url
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config.from_object('professors.config.DevelopmentConfig')

db = SQLAlchemy(app)

jwt = JWTManager(app)

from professors.routes import *