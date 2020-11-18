from quizapp.database import db


class Quiz(db.Model):

    __tablename__ = 'quizs'

    quizID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    problem = db.Column(db.String(100))
    correct = db.Column(db.Boolean)
    userID = db.Column(db.String(20), db.ForeignKey('users.userID'))

    def get_quiz_one(self, id):
        quiz = Quiz.query.get(id)

        return quiz

    def get_quiz_all(self):
        quiz_list = Quiz.query.all()

        return quiz_list

    def get_id_all(self):
        fetch_id_list = Quiz.query.all()
        id_list = list(map(lambda x: x.quizID, fetch_id_list))

        return id_list

    def quiz_count(self):
        quiz_count = Quiz.query.count()

        return quiz_count

    def register_quiz(self, problem, correct, userID):
        record = Quiz(
            problem=problem,
            correct=correct,
            userID=userID
        )

        db.session.add(record)
        db.session.commit()
