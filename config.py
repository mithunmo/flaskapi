
import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/postgres'
SQLALCHEMY_TRACK_MODIFICATIONS = False
REDIS_HOST = "localhost"
REDIS_PORT = "6379"
REDIS_URL = "redis://localhost:6379/0"
