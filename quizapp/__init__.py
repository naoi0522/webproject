from flask import *
from quizapp.database import init_db
import quizapp.models
import quizapp.config
from quizapp.buildjson import *

#app = Flask(__name__)

bjson = BuildJSON()


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('quizapp.config.Config')
    app.config["JSON_AS_ASCII"] = False
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

    init_db(app)

    @app.route('/', methods=['GET'])
    def index():
        if not 'userID' in session:
            session['userID'] = None
        if not 'login' in session:
            session['login'] = False

        login_status = bjson.build_login_status(
            session['userID'], session['login'])

        # return jsonify(login_status)

        return render_template('index.html',
                               title="メインページ", current_userID=session['userID'], login=session['login'])

    from . import auth
    app.register_blueprint(auth.bp)

    from . import quiz
    app.register_blueprint(quiz.bp)

    from . import mypage
    app.register_blueprint(mypage.bp)

    return app
