import os
import pyodbc 
basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    #Database URL
    SQLALCHEMY_DATABASE_URI = 'DRIVER={Devart ODBC Driver for SQL Server};Server=localhost;Database=testdbaccess;Port=1433;User ID=desa;Password=desa'

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
