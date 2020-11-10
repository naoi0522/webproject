from DBaccess import *


class QuizManage:
    def __init__(self, dbac):
        self.dbac = dbac
        self.count = self.dbac.quiz_count()

    def select_quiz(self):
        self.rows = self.dbac.select()
