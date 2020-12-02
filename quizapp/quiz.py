# import functools
from time import sleep
from quizapp.quizmanage import *
from flask import(
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from quizapp.utils import prepare_response
# from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('quiz', __name__, url_prefix='/quiz')


@bp.route('newquiz', methods=['GET'])
def newquiz():
    session['quiz_num'], session['correct_total'], session['order'] = QuizManage.new_quiz()

    session['quiz_num'], problem = QuizManage.get_next_quiz(
        session['quiz_num'], json.loads(session['order']))

    response_body = render_template('quiz/quiz.html',
                                    title="クイズ", current_userID=session['userID'], login=session['login'],
                                    answered=False, quiz_num=session['quiz_num'], problem=problem)
    response = prepare_response(response_body)
    return response


@bp.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == "POST":
        ans = request.form['ans']
        result, session['correct_total'], problem = QuizManage.judge(
            ans, session['quiz_num'], session['correct_total'], json.loads(session['order']))

        response_body = render_template('quiz/quiz.html',
                                        title="クイズ", current_userID=session['userID'], login=session['login'],
                                        answered=True, quiz_num=session['quiz_num'], problem=problem, ans=ans, result=result)
        response = prepare_response(response_body)
        return response

    else:
        session['quiz_num'], problem = QuizManage.get_next_quiz(
            session['quiz_num'], json.loads(session['order']))

        response_body = render_template('quiz/quiz.html',
                                        title="クイズ", current_userID=session['userID'], login=session['login'],
                                        answered=False, quiz_num=session['quiz_num'], problem=problem)
        response = prepare_response(response_body)
        return response


@bp.route('/result', methods=['GET'])
def result():
    response_body = render_template('quiz/result.html',
                                    title="結果発表", current_userID=session['userID'], login=session['login'],
                                    total=session['correct_total'])
    response = prepare_response(response_body)
    return response


@bp.route('/registerquiz', methods=['GET', 'POST'])
def registerquiz():
    if request.method == "POST":
        problem = request.form['problem']
        correct = int(request.form['correct'])
        userID = session['userID']

        correct = QuizManage.register_quiz(problem, correct, userID)
        response_body = render_template('quiz/registerquiz.html',
                                        title="クイズ登録", current_userID=session['userID'], login=session['login'],
                                        is_post=True, correct=correct)
        response = prepare_response(response_body)
        return response
    else:
        response_body = render_template('quiz/registerquiz.html',
                                        title="クイズ登録", current_userID=session['userID'], login=session['login'],
                                        is_post=False)
        response = prepare_response(response_body)
        return response


@bp.route('/update', methods=['GET', 'POST'])
def updatequiz():
    if request.method == "POST":
        quizID = int(request.form['quizID'])
        problem = request.form['problem']
        correct = int(request.form['correct'])

        correct = QuizManage.update_quiz(quizID, problem, correct)

        response_body = render_template('quiz/update.html',
                                        title="クイズ更新", current_userID=session['userID'], login=session['login'],
                                        is_post=True, correct=correct)
        response = prepare_response(response_body)
        return response

    else:
        response_body = render_template('quiz/update.html',
                                        title="クイズ更新", current_userID=session['userID'], login=session['login'],
                                        is_post=False)
        response = prepare_response(response_body)
        return response


@bp.route('/delete', methods=['GET', 'POST'])
def deletequiz():
    if request.method == "POST":
        quizID = int(request.form['quizID'])

        QuizManage.delete_quiz(quizID)

        response_body = render_template('quiz/delete.html',
                                        title="クイズ削除", current_userID=session['userID'], login=session['login'],
                                        is_post=True)
        response = prepare_response(response_body)
        return response

    else:
        response_body = render_template('quiz/delete.html',
                                        title="クイズ削除", current_userID=session['userID'], login=session['login'],
                                        is_post=False)
        response = prepare_response(response_body)
        return response
