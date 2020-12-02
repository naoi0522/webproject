#import functools
import time
from quizapp.quizmanage import *
from quizapp.usermanage import *
from quizapp.utils import prepare_response
from flask import(
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
#from werkzeug.security import check_password_hash, generate_password_hash


bp = Blueprint('mypage', __name__, url_prefix='/mypage')


@bp.route('/<user_id>', methods=['GET'])
def mypage(user_id):
    quiz_list = QuizManage.get_quiz_from_userID(user_id)
    quiz_count = 4 if len(quiz_list) > 4 else 0

    response_body = render_template('mypage/mypage.html',
                                    title="マイページ", current_userID=session['userID'], login=session['login'],
                                    quiz_list=quiz_list, quiz_count=quiz_count, param=user_id)

    response = prepare_response(response_body)
    return response
