from flask import *
from quizapp.database import init_db
import quizapp.models
from quizapp.quizmanage import *
import quizapp.config


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    # 本番と開発切り替え
    app.config.from_object('quizapp.config.DevConfig')

    init_db(app)

    @app.route('/', methods=['GET', 'POST'])
    def index():
        if not 'userID' in session:
            session['userID'] = None
        if not 'login' in session:
            session['login'] = False
        return render_template('index.html',
                               title="メインページ", current_userID=session['userID'], login=session['login'])

    from . import auth
    app.register_blueprint(auth.bp)

    from . import quiz
    app.register_blueprint(quiz.bp)

    from . import mypage
    app.register_blueprint(mypage.bp)

    return app
