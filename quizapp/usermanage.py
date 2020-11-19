from quizapp.models.user import User


class UserManage():

    def __init__(self):
        self.user = User()

    def check_duplication(self, userID):
        duplicate = self.user.get_user_one(userID)

        if not duplicate == None:
            return True
        else:
            return False

    def register_user(self, userID, passwd):
        if not self.check_duplication(userID):
            #self.user.register_user(userID, passwd)
            return True
        else:
            return False

    def check_password(self, userID, passwd):
        saved_user = self.user.get_user_one(userID)

        if saved_user.password == passwd:
            return True
        else:
            return False

    def authenticate_user(self, userID, passwd):
        if self.check_duplication(userID):
            if self.check_password(userID, passwd):
                return True
            else:
                return False
        else:
            return False
