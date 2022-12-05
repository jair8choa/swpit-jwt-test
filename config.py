import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    SQL_CLOUD_PASSWORD = os.environ.get('SQL_CLOUD_PASSWORD')
    SQL_LOCAL_PASSWORD = os.environ.get('SQL_LOCAL_PASSWORD')

class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:{}@35.225.253.13:3306/swpit'.format(Config.SQL_CLOUD_PASSWORD)
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:{}@localhost:3306/swpit'.format(Config.SQL_LOCAL_PASSWORD)
    SQLALCHEMY_TRACK_MODIFICATIONS = False