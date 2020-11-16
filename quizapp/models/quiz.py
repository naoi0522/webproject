from quizapp.database import db


class Quiz(db.Model):

    __tablename__ = 'quizs'

    quizID = db.Column(db.Integer, primary_key=True)
    problem = db.Column(db.String(100))
    correct = db.Column(db.Boolean)

    def get_quiz_one(self, id):
        quiz = db.session.query(Quiz).get(id)

        return quiz

    def get_quiz_all(self):
        quiz_list = db.session.query(Quiz).all()

        return quiz_list

    def quiz_count(self):
        quiz_count = db.session.query(Quiz).count()

        return quiz_count

    def register_quiz(self, quizID, problem, correct):
        record = Quiz(
            quizID=quizID,
            problem=problem,
            correct=correct
        )

        db.session.add(record)
        db.session.commit()
