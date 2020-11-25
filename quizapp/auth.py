#import functools
from quizapp.usermanage import *
from quizapp.buildjson import *
from flask import(
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
#from werkzeug.security import check_password_hash, generate_password_hash


bp = Blueprint('auth', __name__, url_prefix='/auth')
umng = UserManage()
bjson = BuildJSON()


@bp.route('/registeruser', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        userID = request.form['userID']
        passwd = request.form['passwd']

        CRUD_correct = umng.register_user(userID, passwd)

        if CRUD_correct:
            session['userID'] = userID
            session['login'] = CRUD_correct
        else:
            session['userID'] = None
            session['login'] = CRUD_correct

        login_status = bjson.build_login_status(
            session['userID'], session['login'])
        status = bjson.build_status(request.method, "")
        user = bjson.build_user(userID, "")

        # return jsonify(login_status, status, user)

        return render_template('auth/registeruser.html',
                               title="ユーザ登録", current_userID=session['userID'], login=session['login'], is_post=True, userID=userID)
    else:
        status = bjson.build_status(request.method, "")

        # return jsonify(status)

        return render_template('auth/registeruser.html',
                               title="ユーザ登録", current_userID=session['userID'], login=session['login'], is_post=False)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        userID = request.form['userID']
        passwd = request.form['passwd']

        CRUD_correct = umng.authenticate_user(userID, passwd)

        if CRUD_correct:
            session['userID'] = userID
            session['login'] = CRUD_correct
        else:
            session['userID'] = None
            session['login'] = CRUD_correct

        login_status = bjson.build_login_status(
            session['userID'], session['login'])
        status = bjson.build_status(request.method, "")
        user = bjson.build_user(userID, "")

        # return jsonify(login_status, status, user)

        return render_template('auth/login.html',
                               title="ログイン", current_userID=session['userID'], login=session['login'], is_post=True, userID=userID)
    else:
        status = bjson.build_status(request.method, "")

        # return jsonify(status)

        return render_template('auth/login.html',
                               title="ログイン", current_userID=session['userID'], login=session['login'], is_post=False)


@bp.route('/logout', methods=['GET'])
def logout():
    session.pop('userID', None)
    session['login'] = False

    login_status = bjson.build_login_status(
        session['userID'], session['login'])

    # return jsonify(login_status)

    return redirect(url_for('index'))
