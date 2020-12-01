import os
import os


class Config:

    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'


class ProductConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('PROD_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/'

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}:{port}/webquizapp?charset=utf8'.format(**{
        'user': 'root',
        'password': 'tbctbctbc',
        'host': 'localhost',
        'port': '3306'
    })
    SQLALCHEMY_TRACK_MODIFICATIONS = False
