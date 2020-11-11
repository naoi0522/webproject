class SystemConfig:

    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}:{port}/webquizapp?charset=utf8'.format(**{
        'user': 'root',
        'password': 'tbctbctbc',
        'host': 'localhost',
        'port': '3306'
    })
    SQLALCHEMY_TRACK_MODIFICATIONS = False


Config = SystemConfig
