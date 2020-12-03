from quizapp.database import db


class Quiz(db.Model):

    __tablename__ = 'quizs'

    quizID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    problem = db.Column(db.String(100))
    correct = db.Column(db.Boolean)
    userID = db.Column(db.String(20), db.ForeignKey('users.userID'))

    @staticmethod
    def get_quiz_one(id):
        return Quiz.query.get(id)

    @classmethod
    def get_quiz_from_userID(cls, userID):
        return cls.query.filter(Quiz.userID == userID).all()

    @classmethod
    def get_quiz_all(cls):
        return cls.query.all()

    @classmethod
    def get_id_all(cls):
        fetch_id_list = cls.query.all()
        return list(map(lambda x: x.quizID, fetch_id_list))

    @classmethod
    def quiz_count(cls):
        return cls.query.count()

    @classmethod
    def register_quiz(cls, problem, correct, userID):
        record = cls(
            problem=problem,
            correct=correct,
            userID=userID
        )

        db.session.add(record)
        db.session.commit()

    @classmethod
    def update_quiz(cls, quizID, problem, correct):
        quiz = cls.get_quiz_one(quizID)

        quiz.problem = problem
        quiz.correct = correct

        db.session.commit()

    @classmethod
    def delete_quiz_one(cls, quizID):
        cls.get_quiz_one(quizID).delete()

        db.session.commit()

    @classmethod
    def delete_quiz_from_userID(cls, userID):
        cls.filter(cls.userID == userID).delete()

        db.session.commit()
