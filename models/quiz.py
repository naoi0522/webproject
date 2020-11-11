from database import db


class Quiz(db.Model):

    __tablename__ = 'quizs'

    quizID = db.Column(db.Integer, primary_key=True)
    problem = db.Column(db.String(100))
    correct = db.Column(db.Boolean)
