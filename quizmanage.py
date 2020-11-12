from sqlalchemy.sql.elements import Null
from models.quiz import Quiz
import random


class QuizManage():

    def __init__(self):
        self.quiz = Quiz()
        self.quiz_num = 0
        self.quiz_order()
        # self.count = self.quiz.quiz_count() self.quiz.quiz_countがエラーになる

    def quiz_order(self):
        self.order = list(range(10))
        random.shuffle(self.order)

    def next_quiz(self):
        if self.quiz_num < 10:
            quiz = self.get_quiz(self.order[self.quiz_num])
            self.quiz_num += 1
        else:
            self.quiz_num = 0
            quiz = Null

        return quiz

    def get_quiz(self, id):
        quiz = self.quiz.get_quiz_one(1)  # testcode

        print(quiz.problem)
        return quiz

    def register_quiz(self, problem, correct):
        id = self.quiz.quiz_count() + 1

        self.quiz.register_quiz(id, problem, correct)
