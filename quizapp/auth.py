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

        success = umng.register_user(userID, passwd)

        return render_template('auth/registeruser.html', is_post=True, userID=userID, success=success)
    else:
        return render_template('auth/registeruser.html', is_post=False)
