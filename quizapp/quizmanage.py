from flask_migrate import current
from sqlalchemy.inspection import inspect
from quizapp.models.quiz import Quiz
from quizapp.checkstring import CheckString
from sqlalchemy.sql.expression import func, select
import random
import json


class QuizManage():

    def __init__(self):
        pass

    @classmethod
    def new_quiz(cls):
        return 0, 0, json.dumps(cls.set_order())

    @staticmethod
    def set_quiz_count():
        return Quiz.quiz_count()

    @staticmethod
    def set_order():
        return random.sample(Quiz.get_id_all(), 10)

    @classmethod
    def get_next_quiz(cls, quiz_num, order):
        if quiz_num < 10:
            current_quiz = cls.get_quiz(order[quiz_num])

            return quiz_num + 1, current_quiz.problem
        else:
            return 0, None

    @staticmethod
    def get_quiz(id):
        return Quiz.get_quiz_one(id)

    @staticmethod
    def get_quiz_from_userID(userID):
        return Quiz.get_quiz_from_userID(userID)

    @classmethod
    def judge(cls, ans, quiz_num, correct_total, order):
        if ans == "True":
            ans = True
        else:
            ans = False
        # get_next_quizによりquiz_numは加算されているため、1を引いて調整
        current_quiz = cls.get_quiz(order[quiz_num - 1])

        if ans == current_quiz.correct:
            result = True
            correct_total += 1
        else:
            result = False

        return result, correct_total, current_quiz.problem,

    @staticmethod
    def register_quiz(problem, correct, userID):
        problem = CheckString.trim_spaces(problem)

        if CheckString.check_str_length(problem, 6):
            Quiz.register_quiz(problem, correct, userID)
            # TODO クイズ追加on/off
            return True
        else:
            return False

    @staticmethod
    def update_quiz(quizID, problem, correct):
        problem = CheckString.trim_spaces(problem)

        if CheckString.check_str_length(problem, 6):
            #Quiz.update_quiz(quizID, problem, correct)
            # TODO クイズ更新on/off
            return True
        else:
            return False

    @staticmethod
    def delete_quiz(quizID):
        Quiz.delete_quiz_one(quizID)

    @staticmethod
    def delete_quiz_from_userID(userID):
        Quiz.delete_quiz_from_userID(userID)
