import os


# def get_env_variable(name):
#     try:
#         return os.environ.get(name)
#     except KeyError:
#         message = "Expected environment variable '{}' not set.".format(name)
#         raise Exception(message)


# get env vars OR ELSE
# POSTGRES_URL = get_env_variable("POSTGRES_URL")  # 5432
# POSTGRES_USER = get_env_variable("POSTGRES_USER")
# POSTGRES_PW = get_env_variable("POSTGRES_PW")
# POSTGRES_DB = get_env_variable("POSTGRES_DB")
#
# DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER, pw=POSTGRES_PW, url=POSTGRES_URL,
#                                                                db=POSTGRES_DB)

DEBUG = True

SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://gametime:smilecook1!@localhost:5432/smilecook"
# SQLALCHEMY_DATABASE_URI = DB_URL
SQLALCHEMY_TRACK_MODIFICATIONS = False
