#import functools
from quizapp.quizmanage import *
from quizapp.usermanage import *

from flask import(
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
#from werkzeug.security import check_password_hash, generate_password_hash


bp = Blueprint('mypage', __name__, url_prefix='/mypage')
qmng = QuizManage()
umng = UserManage()


@bp.route('/', methods=['GET'])
def mypage():
    quiz_list = qmng.get_quiz_from_userID(session['userID'])
    quiz_count = 0
    for quiz in quiz_list:
        quiz_count += 1
        if quiz_count > 4:
            break

    return render_template('mypage/mypage.html',
                           title="マイページ", current_userID=session['userID'], login=session['login'],
                           quiz_list=quiz_list, quiz_count=quiz_count)
