from sqlalchemy.sql.schema import PrimaryKeyConstraint
from quizapp.database import db


class User(db.Model):

    __tablename__ = 'users'

    userID = db.Column(db.String(20), primary_key=True)
    password = db.Column(db.String(64))
    quizs = db.relationship('Quiz', backref='user')

    def get_user_one(self, userID):
        user = User.query.get(userID)

        return user

    def get_user_all(self):
        user_list = User.query.all()

        return user_list

    def user_count(self):
        user_count = User.query.count()

        return user_count

    def register_user(self, userID, password):
        record = User(
            userID=userID,
            password=password
        )

        db.session.add(record)
        db.session.commit()

    def change_password(self, userID, password):
        user = self.get_quiz_one(userID)

        user.password = password

        db.session.commit()

    def delete_user(self, userID):
        db.session.query(User).filter(User.userID == userID).delete()

        db.session.commit()
