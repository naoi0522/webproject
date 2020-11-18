#import functools
from quizapp.quizmanage import *
from flask import(
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
#from werkzeug.security import check_password_hash, generate_password_hash


bp = Blueprint('quiz', __name__, url_prefix='/quiz')
qmng = QuizManage()


@bp.route('newquiz', methods=['GET'])
def newquiz():
    qmng.new_quiz()

    quiz_num, problem = qmng.get_next_quiz()
    return render_template('quiz/quiz.html',
                           title="クイズ", current_userID=session['userID'], login=session['login'],
                           answered=False, quiz_num=quiz_num, problem=problem)


@bp.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == "POST":
        ans = request.form['ans']
        result, quiz_num, problem = qmng.judge(ans)
        return render_template('quiz/quiz.html',
                               title="クイズ", current_userID=session['userID'], login=session['login'],
                               answered=True, quiz_num=quiz_num, problem=problem, ans=ans, result=result)
    else:
        quiz_num, problem = qmng.get_next_quiz()
        return render_template('quiz/quiz.html',
                               title="クイズ", current_userID=session['userID'], login=session['login'],
                               answered=False, quiz_num=quiz_num, problem=problem)


@bp.route('/result', methods=['GET'])
def result():
    total = qmng.get_correct_total()
    return render_template('quiz/result.html',
                           title="結果発表", current_userID=session['userID'], login=session['login'],
                           total=total)


@bp.route('/registerquiz', methods=['GET', 'POST'])
def registerquiz():
    if request.method == "POST":
        problem = request.form['problem']
        correct = int(request.form['correct'])
        userID = session['userID']

        qmng.register_quiz(problem, correct, userID)

        # TODO 入力値の制限(空白など),登録可否での処理の変更

        return render_template('quiz/registerquiz.html',
                               title="クイズ登録", current_userID=session['userID'], login=session['login'])
    else:
        return render_template('quiz/registerquiz.html',
                               title="クイズ登録", current_userID=session['userID'], login=session['login'])
