class SystemConfig:

    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{user}:{password}@{host}[:{port}]/webquizapp'.format(**{
        'user': 'root',
        'password': 'tbctbctbc',
        'host': 'localhost',
        'port': '3306'
    })
    SQLALCHEMY_TRACK_MODIFICATIONS = False

Config = SystemConfig