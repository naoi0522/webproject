from sqlalchemy.sql.schema import PrimaryKeyConstraint
from quizapp.database import db


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(60), nullable=False)
    quizs = db.relationship('Quiz', backref='user')
    stores = db.relationship('Store', backref="owner")

    # def get_user_one(self, userID):
    #     user = User.query.get(userID)

    #     return user

    # def get_user_all(self):
    #     user_list = User.query.all()

    #     return user_list

    # def user_count(self):
    #     user_count = User.query.count()

    #     return user_count

    # def register_user(self, userID, password):
    #     record = User(
    #         userID=userID,
    #         password=password
    #     )

    #     db.session.add(record)
    #     db.session.commit()

    # def change_password(self, userID, password):
    #     user = self.get_quiz_one(userID)

    #     user.password = password

    #     db.session.commit()

    # def delete_user(self, userID):
    #     self.get_user_one(userID).delete()

    #     db.session.commit()
