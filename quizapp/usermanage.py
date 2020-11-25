from quizapp.models.user import User
from quizapp.checkstring import *


class UserManage():

    def __init__(self):
        self.user = User()
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

        if self.cstr.check_str_length(userID, 3) and self.cstr.check_str_length(passwd, 6):
            if not self.check_duplication(userID):
                #self.user.register_user(userID, passwd)
                # TODO ユーザ登録on/off
                return True

        return False

    def check_password(self, userID, passwd):
        saved_user = self.user.get_user_one(userID)

        if saved_user.password == passwd:
            return True
        else:
            return False

    def authenticate_user(self, userID, passwd):
        userID = self.cstr.trim_spaces(userID)
        passwd = self.cstr.trim_spaces(passwd)

        if self.cstr.check_str_length(userID, 3) and self.cstr.check_str_length(passwd, 6):
            if self.check_duplication(userID):
                if self.check_password(userID, passwd):
                    return True

        return False

    def delete_user(self, qmng, userID, passwd):
        if self.check_password(userID, passwd):
            # TODO 作る qmng.delete_quiz_from_userID(userID)
            self.user.delete_user(userID)

            return True
        else:
            return False
