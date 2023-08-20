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