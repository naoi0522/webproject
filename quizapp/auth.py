import functools
from quizapp.usermanage import *
from flask import(
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash


bp = Blueprint('auth', __name__, url_prefix='/auth')
umng = UserManage()


@bp.route('/registeruser', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        userID = request.form['userID']
        passwd = request.form['passwd']

        session['login'] = umng.register_user(userID, passwd)

        if session['login']:
            session['userID'] = userID
        else:
            session['userID'] = None

        return render_template('auth/registeruser.html',
                               title="ユーザ登録", current_userID=session['userID'], login=session['login'], is_post=True, userID=userID)
    else:
        return render_template('auth/registeruser.html',
                               title="ユーザ登録", current_userID=session['userID'], login=session['login'], is_post=False)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        userID = request.form['userID']
        passwd = request.form['passwd']

        session['login'] = umng.authenticate_user(userID, passwd)

        if session['login']:
            session['userID'] = userID
        else:
            session['userID'] = None

        return render_template('auth/login.html',
                               title="ログイン", current_userID=session['userID'], login=session['login'], is_post=True, userID=userID)
    else:
        return render_template('auth/login.html',
                               title="ログイン", current_userID=session['userID'], login=session['login'], is_post=False)


@bp.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('userID', None)
    session['login'] = False

    return redirect(url_for('index'))
