from quizapp.database import db


class Quiz(db.Model):

    __tablename__ = 'quizs'

    quiz_id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100))
    correct = db.Column(db.Boolean)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    # create_user = db.relationship(
    # 'User', backref='quizs', cascade='delete,all')

    # def get_quiz_one(self, id):
    #     quiz = Quiz.query.get(id)

    #     return quiz

    # def get_quiz_from_userID(self, userID):
    #     quiz_list = Quiz.query.filter(Quiz.userID == userID).all()

    #     return quiz_list

    # def get_quiz_all(self):
    #     quiz_list = Quiz.query.all()

    #     return quiz_list

    # def get_id_all(self):
    #     fetch_id_list = Quiz.query.all()
    #     id_list = list(map(lambda x: x.quizID, fetch_id_list))

    #     return id_list

    # def quiz_count(self):
    #     quiz_count = Quiz.query.count()

    #     return quiz_count

    # def register_quiz(self, problem, correct, userID):
    #     record = Quiz(
    #         problem=problem,
    #         correct=correct,
    #         userID=userID
    #     )

    #     db.session.add(record)
    #     db.session.commit()

    # def update_quiz(self, quizID, problem, correct):
    #     quiz = self.get_quiz_one(quizID)

    #     quiz.problem = problem
    #     quiz.correct = correct

    #     db.session.commit()

    # def delete_quiz_one(self, quizID):
    #     self.get_quiz_one(quizID).delete()

    #     db.session.commit()

    # def delete_quiz_from_userID(self, userID):
    #     self.get_quiz_from_userID(userID).delete()

    #     db.session.commit()
