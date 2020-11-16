from quizapp.models.user import User


class UserManage():

    def __init__(self):
        self.user = User()

    def duplication_check(self, userID):
        duplicate = self.user.get_user_one(userID)

        if duplicate == None:
            return True
        else:
            return False

    def register_user(self, userID, passwd):
        if self.duplication_check(userID):
            #self.user.register_user(userID, passwd)
            return True
        else:
            return False
