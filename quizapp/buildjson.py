from flask.json import jsonify


class BuildJSON():
    def build_login_status(self, userID, login):
        login_status = {
            "userID": "{}".format(userID),
            "login": "{}".format(login)
        }

        return login_status

    def build_status(self, method, CRUD_correct):
        status = {
            "method": "{}".format(method),
            "CRUD_correct": "{}".format(CRUD_correct)
        }

        return status

    def build_quiz(self, quizID, problem, correct, userID):
        quiz = {
            "quizID": "{}".format(quizID),
            "problem": "{}".format(problem),
            "correct": "{}".format(correct),
            "userID": "{}".format(userID)
        }

        return quiz

    def build_quiz_info(self, quiz_num, answered, ans, result, total):
        quiz_info = {
            "quiz_num": "{}".format(quiz_num),
            "answered": "{}".format(answered),
            "ans": "{}".format(ans),
            "result": "{}".format(result),
            "total": "{}".format(total)
        }

        return quiz_info

    def build_user(self, userID, passwd):
        user = {
            "userID": "{}".format(userID),
            "passwd": "{}".format(passwd)
        }

        return user
