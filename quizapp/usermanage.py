from quizapp.models.user import User
from quizapp.quizmanage import QuizManage
from quizapp.checkstring import CheckString
import hashlib


class UserManage():

    def __init__(self):
        self.user = User()
        self.qmng = QuizManage()
        self.cstr = CheckString()

    def check_duplication(self, userID):
        duplicate = self.user.get_user_one(userID)

        if not duplicate == None:
            return True
        else:
            return False

    def register_user(self, userID, passwd):
        userID = self.cstr.trim_spaces(userID)
        passwd = self.cstr.trim_spaces(passwd)

        if not self.check_duplication(userID):
            if self.cstr.check_str_length(userID, 3) and self.cstr.check_str_length(passwd, 6):
                hashed_pass = hashlib.sha256(passwd.encode()).hexdigest()
                self.user.register_user(userID, hashed_pass)
                # TODO ユーザ登録on/off
                message = "ようこそ、" + userID + "さん。"
                return userID, True, message
            else:
                message = "文字数が足りていません。"
                return userID, False, message
        else:
            message = "ユーザID : " + userID + "は既に存在します。"
            return userID, False, message

    def check_password(self, userID, passwd):
        saved_user = self.user.get_user_one(userID)
        hashed_pass = hashlib.sha256(passwd.encode()).hexdigest()

        if saved_user.password == hashed_pass:
            return True
        else:
            return False

    def authenticate_user(self, userID, passwd):
        if self.check_duplication(userID):
            if self.check_password(userID, passwd):
                return userID, True
        return userID, False

    def delete_user(self, userID, passwd):
        if self.check_password(userID, passwd):
            self.qmng.delete_quiz_from_userID(userID)
            self.user.delete_user(userID)

            return True
        else:
            return False
