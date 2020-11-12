from models.quiz import Quiz


class QuizManage():

    def register_quiz(self, problem, correct):
        id = 1

        Quiz.register_quiz(id, problem, correct)
