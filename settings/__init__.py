import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_TYPE = "postgresql"
#DB_TYPE = "sqlite"
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_INST = os.environ.get('DB_INST')

class Config(object):
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
    #SQLALCHEMY_DATABASE_URI = "postgresql://postgres:mysecretpassword@localhost:5432/postgres"
    SQLALCHEMY_DATABASE_URI = DB_TYPE + ':///' + DB_USER + ":" DB_PASSWORD + "@" + DB_HOST + ":" + DB_PORT + "/" + DB_INST