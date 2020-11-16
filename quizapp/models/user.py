from sqlalchemy.sql.schema import PrimaryKeyConstraint
from quizapp.database import db


class User(db.Model):

    __tablename__ = 'users'

    userID = db.Column(db.String(20), primary_key=True)
    password = db.Column(db.String(20))
