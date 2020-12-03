from sqlalchemy.sql.schema import PrimaryKeyConstraint
from quizapp.database import db


class User(db.Model):

    __tablename__ = 'users'

    userID = db.Column(db.String(20), primary_key=True)
    password = db.Column(db.String(64))
    quizs = db.relationship('Quiz', backref='user')

    @classmethod
    def get_user_one(cls, userID):
        return cls.query.get(userID)

    @classmethod
    def get_user_all(cls):
        return cls.query.all()

    @classmethod
    def user_count(cls):
        return cls.query.count()

    @classmethod
    def register_user(cls, userID, password):
        record = cls(
            userID=userID,
            password=password
        )

        db.session.add(record)
        db.session.commit()

    @classmethod
    def change_password(cls, userID, password):
        user = cls.get_user_one(userID)
        user.password = password

        db.session.commit()

    @classmethod
    def delete_user(cls, userID):
        cls.filter(cls.userID == userID).delete()

        db.session.commit()
