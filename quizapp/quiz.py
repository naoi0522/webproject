#import functools
from quizapp.quizmanage import *
from quizapp.buildjson import *
from flask import(
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
#from werkzeug.security import check_password_hash, generate_password_hash


bp = Blueprint('quiz', __name__, url_prefix='/quiz')
qmng = QuizManage()
bjson = BuildJSON()


@bp.route('newquiz', methods=['GET'])
def newquiz():
    qmng.new_quiz()

    quiz_num, problem = qmng.get_next_quiz()

    quiz_info = bjson.build_quiz_info(quiz_num, False, "", "", "")
    quiz = bjson.build_quiz("", problem, "", "")

    # return jsonify(quiz_info, quiz)

    return render_template('quiz/quiz.html',
                           title="クイズ", current_userID=session['userID'], login=session['login'],
                           answered=False, quiz_num=quiz_num, problem=problem)


@bp.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == "POST":
        ans = request.form['ans']
        result, quiz_num, problem = qmng.judge(ans)

        quiz_info = bjson.build_quiz_info(quiz_num, True, ans, result, "")
        quiz = bjson.build_quiz("", problem, "", "")

        # return jsonify(quiz_info, quiz)

        return render_template('quiz/quiz.html',
                               title="クイズ", current_userID=session['userID'], login=session['login'],
                               answered=True, quiz_num=quiz_num, problem=problem, ans=ans, result=result)
    else:
        quiz_num, problem = qmng.get_next_quiz()

        quiz_info = bjson.build_quiz_info(quiz_num, False, "", "", "")
        quiz = bjson.build_quiz("", problem, "", "")

        # return jsonify(quiz_info, quiz)

        return render_template('quiz/quiz.html',
                               title="クイズ", current_userID=session['userID'], login=session['login'],
                               answered=False, quiz_num=quiz_num, problem=problem)


@bp.route('/result', methods=['GET'])
def result():
    total = qmng.get_correct_total()

    quiz_info = bjson.build_quiz_info("", "", "", "", total)

    # return jsonify(quiz_info)

    return render_template('quiz/result.html',
                           title="結果発表", current_userID=session['userID'], login=session['login'],
                           total=total)


@bp.route('/registerquiz', methods=['GET', 'POST'])
def registerquiz():
    if request.method == "POST":
        problem = request.form['problem']
        correct = int(request.form['correct'])
        userID = session['userID']

        CRUD_correct = qmng.register_quiz(problem, correct, userID)

        status = bjson.build_status(request.method, CRUD_correct)

        # return jsonify(status)

        return render_template('quiz/registerquiz.html',
                               title="クイズ登録", current_userID=session['userID'], login=session['login'],
                               is_post=True, correct=correct)
    else:
        status = bjson.build_status(request.method, "")

        # return jsonify(status)

        return render_template('quiz/registerquiz.html',
                               title="クイズ登録", current_userID=session['userID'], login=session['login'],
                               is_post=False)


@bp.route('/update', methods=['GET', 'POST'])
def updatequiz():
    if request.method == "POST":
        quizID = int(request.form['quizID'])
        problem = request.form['problem']
        correct = int(request.form['correct'])

        CRUD_correct = qmng.update_quiz(quizID, problem, correct)

        status = bjson.build_status(request.method, CRUD_correct)

        # return jsonify(status)

        return render_template('quiz/update.html',
                               title="クイズ更新", current_userID=session['userID'], login=session['login'],
                               is_post=True, correct=correct)
    else:
        status = bjson.build_status(request.method, "")

        # return jsonify(status)

        return render_template('quiz/update.html',
                               title="クイズ更新", current_userID=session['userID'], login=session['login'],
                               is_post=False)
