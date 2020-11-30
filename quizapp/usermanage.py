from quizapp.models.user import User
from quizapp.checkstring import CheckString


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

        if not self.check_duplication(userID):
<<<<<<< HEAD
            self.user.register_user(userID, passwd)
            # TODO ユーザ登録on/off
            return True
        else:
            return False
=======
            if self.cstr.check_str_length(userID, 3) and self.cstr.check_str_length(passwd, 6):
                #self.user.register_user(userID, passwd)
                # TODO ユーザ登録on/off
                return userID, True
        return userID, False
>>>>>>> d76ea9a89ce16e8556e753ed6129bbf475314977

    def check_password(self, userID, passwd):
        saved_user = self.user.get_user_one(userID)

        if saved_user.password == passwd:
            return True
        else:
            return False

    def authenticate_user(self, userID, passwd):
        if self.check_duplication(userID):
            if self.check_password(userID, passwd):
                return userID, True
        return userID, False

    def delete_user(self, qmng, userID, passwd):
        if self.check_password(userID, passwd):
            # qmng.delete_quiz_from_userID(userID)
            # TODO　作る
            self.user.delete_user(userID)

            return True
        else:
            return False
