from sqlalchemy.inspection import inspect
from quizapp.models.quiz import Quiz
from quizapp.checkstring import CheckString
from sqlalchemy.sql.expression import func, select
import random


class QuizManage():

    def __init__(self):
        self.quiz = Quiz()
        self.cstr = CheckString()

    def new_quiz(self):
        self.quiz_num = 0
        self.correct_total = 0
        self.set_order()

    def set_quiz_count(self):
        self.count = self.quiz.quiz_count()

    def set_order(self):
        self.order = random.sample(self.quiz.get_id_all(), 10)

    def get_next_quiz(self):
        if self.quiz_num < 10:
            self.current_quiz = self.get_quiz(self.order[self.quiz_num])
            self.quiz_num += 1

            return self.quiz_num, self.current_quiz.problem
        else:
            self.quiz_num = 0
            return self.quiz_num, None

    def get_quiz(self, id):
        quiz = self.quiz.get_quiz_one(id)

        return quiz

    def get_quiz_from_userID(self, userID):
        quiz_list = self.quiz.get_quiz_from_userID(userID)

        return quiz_list

    def get_correct_total(self):
        return self.correct_total

    def judge(self, ans):
        if ans == "True":
            ans = True
        else:
            ans = False

        if ans == self.current_quiz.correct:
            result = True
            self.correct_total += 1
        else:
            result = False

        return result, self.quiz_num, self.current_quiz.problem

    def register_quiz(self, problem, correct, userID):
        problem = self.cstr.trim_spaces(problem)

<<<<<<< HEAD
        if self.check_str_length(problem):
            self.quiz.register_quiz(problem, correct, userID)
=======
        if self.cstr.check_str_length(problem, 6):
            #self.quiz.register_quiz(problem, correct, userID)
>>>>>>> d76ea9a89ce16e8556e753ed6129bbf475314977
            # TODO クイズ追加on/off
            return True
        else:
            return False

    def update_quiz(self, quizID, problem, correct):
        problem = self.cstr.trim_spaces(problem)

        if self.cstr.check_str_length(problem, 6):
            #self.quiz.update_quiz(quizID, problem, correct)
            # TODO クイズ更新on/off
            return True
        else:
            return False
