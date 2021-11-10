import os
from os import environ

pswd = os.environ.get('POSTGRES_PW')

class Config:
    DEBUG=True

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://gametime:{'+pswd+'}@localhost/smilecook'
    SQLALCHEMY_TRACK_MODIFICATIONS = False