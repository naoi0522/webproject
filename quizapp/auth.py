# import functools
from quizapp.usermanage import *
from flask import(
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from quizapp.utils import prepare_response
# from flask_login import logout_user
# from werkzeug.security import check_password_hash, generate_password_hash


bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/registeruser', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        userID = request.form['userID']
        passwd = request.form['passwd']
        userID, session['login'], message = UserManage.register_user(
            userID, passwd)
        if session['login']:
            session['userID'] = userID
        else:
            session['userID'] = None

        response_body = render_template('auth/registeruser.html',
                                        title="Quizs | ユーザ登録", current_userID=session['userID'], login=session['login'], is_post=True, message=message)
        response = prepare_response(response_body)
        return response

        return
    else:
        response_body = render_template('auth/registeruser.html',
                                        title="Quizs | ユーザ登録", current_userID=session['userID'], login=session['login'], is_post=False)
        response = prepare_response(response_body)
        return response


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        userID = request.form['userID']
        passwd = request.form['passwd']
        userID, session['login'] = UserManage.authenticate_user(userID, passwd)
        if session['login']:
            session['userID'] = userID
        else:
            session['userID'] = None
        response_body = render_template('auth/login.html',
                                        title="Quizs | ログイン", current_userID=session['userID'], login=session['login'], is_post=True, userID=userID)
        response = prepare_response(response_body)
        return response
    else:
        response_body = render_template('auth/login.html',
                                        title="Quizs | ログイン", current_userID=session['userID'], login=session['login'], is_post=False)
        response = prepare_response(response_body)
        return response


@bp.route('/delete', methods=['GET', 'POST'])
def delete_user():
    if request.method == "POST":
        userID = session['userID']
        passwd = request.form['passwd']
        correct = UserManage.delete_user(userID, passwd)
        if correct:
            session['userID'] = None
            session['login'] = False

        response_body = render_template('auth/delete.html',
                                        title="Quizs | ユーザ削除", current_userID=session['userID'], login=session['login'], is_post=True, correct=correct)
        response = prepare_response(response_body)
        return response

    else:
        response_body = render_template('auth/delete.html',
                                        title="Quizs | ユーザ削除", current_userID=session['userID'], login=session['login'], is_post=False)
        response = prepare_response(response_body)
        return response


@bp.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('userID', None)
    session['login'] = False
    return redirect(url_for('index'))
