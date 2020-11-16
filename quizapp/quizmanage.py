from models.quiz import Quiz
import random


class QuizManage():

    def __init__(self):
        self.quiz = Quiz()

    def new_quiz(self):
        self.quiz_num = 0
        self.correct_total = 0
        self.set_quiz_count()
        self.set_order()

    def set_quiz_count(self):
        self.count = self.quiz.quiz_count()

    def set_order(self):
        self.order = list(range(self.count))
        random.shuffle(self.order)

    def get_next_quiz(self):
        if self.quiz_num < 10:
            self.current_quiz = self.get_quiz(self.order[self.quiz_num] + 1)
            self.quiz_num += 1

            return self.quiz_num, self.current_quiz.problem
        else:
            self.quiz_num = 0
            return self.quiz_num, None

    def get_quiz(self, id):
        quiz = self.quiz.get_quiz_one(id)

        return quiz

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

    def register_quiz(self, problem, correct):
        id = self.quiz.quiz_count() + 1

        self.quiz.register_quiz(id, problem, correct)
