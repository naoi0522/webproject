from quizapp.models.user import User


class UserManage():

    def __init__(self):
        self.user = User()

    def duplication_check(self, userID):
        duplicate = self.user.get_user_one(userID)

        if not duplicate == None:
            return True
        else:
            return False

    def register_user(self, userID, passwd):
        if not self.duplication_check(userID):
            #self.user.register_user(userID, passwd)
            return True
        else:
            return False

    def password_check(self, userID, passwd):
        saved_user = self.user.get_user_one(userID)

        if saved_user.password == passwd:
            return True
        else:
            return False

    def authenticate_user(self, userID, passwd):
        if self.duplication_check(userID):
            if self.password_check(userID, passwd):
                return True
            else:
                return False
        else:
            return False
