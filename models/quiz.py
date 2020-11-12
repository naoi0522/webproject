from database import db


class Quiz(db.Model):

    __tablename__ = 'quizs'

    quizID = db.Column(db.Integer, primary_key=True)
    problem = db.Column(db.String(100))
    correct = db.Column(db.Boolean)

    @classmethod
    def get_quiz_all(cls):
        quiz_list = db.session.query.all()

        return quiz_list

    @classmethod
    def quiz_count(cls):
        quiz_count = db.session.query.count()

        return quiz_count

    @classmethod
    def register_quiz(cls, quizID, problem, correct):
        record = Quiz(
            quizID=quizID,
            problem=problem,
            correct=correct
        )

        db.session.add(record)
        db.session.commit()
