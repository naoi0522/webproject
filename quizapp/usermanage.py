from quizapp.models.user import User
from quizapp.quizmanage import QuizManage
from quizapp.checkstring import CheckString
import hashlib


class UserManage():

    def __init__(self):
        pass

    @staticmethod
    def check_duplication(userID):
        duplicate = User.get_user_one(userID)

        if not duplicate == None:
            return True
        else:
            return False

    @classmethod
    def register_user(cls, userID, passwd):
        userID = CheckString.trim_spaces(userID)
        passwd = CheckString.trim_spaces(passwd)

        if not cls.check_duplication(userID):
            if CheckString.check_str_length(userID, 3) and CheckString.check_str_length(passwd, 6):
                hashed_pass = hashlib.sha256(passwd.encode()).hexdigest()
                User.register_user(userID, hashed_pass)
                # TODO ユーザ登録on/off
                message = "ようこそ、" + userID + "さん。"
                return userID, True, message
            else:
                message = "文字数が足りていません。"
                return userID, False, message
        else:
            message = "ユーザID : " + userID + "は既に存在します。"
            return userID, False, message

    @staticmethod
    def check_password(userID, passwd):
        saved_user = User.get_user_one(userID)
        hashed_pass = hashlib.sha256(passwd.encode()).hexdigest()

        if saved_user.password == hashed_pass:
            return True
        else:
            return False

    @classmethod
    def authenticate_user(cls, userID, passwd):
        if cls.check_duplication(userID):
            if cls.check_password(userID, passwd):
                return userID, True
        return userID, False

    @classmethod
    def delete_user(cls, userID, passwd):
        if cls.check_password(userID, passwd):
            QuizManage.delete_quiz_from_userID(userID)
            UserManage.delete_user(userID)

            return True
        else:
            return False
