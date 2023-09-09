import os, dotenv
import dotenv
from datetime import timedelta
from decouple import config

dotenv.load_dotenv()

class BaseConfig:
    """Base configuration"""
    TESTING = False
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes = 30)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days = 30)
    JWT_SECRET_KEY = config('JWT_SECRET_KEY')
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']


class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(BaseConfig):
    """Testing configuration"""
    TESTING = True


class ProductionConfig(BaseConfig):
    """Production configuration"""
    pass