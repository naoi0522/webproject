from flask import *
from quizapp.database import init_db
import quizapp.models
from quizapp.quizmanage import *
import quizapp.config
from quizapp.utils import prepare_response


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True,
                static_folder='static', template_folder='templates')
    # 本番と開発切り替え ProductConfig <-> DevConfig
    app.config.from_object('quizapp.config.ProductConfig')
    init_db(app)

    @app.route('/', methods=['GET', 'POST'])
    def index():
        if not 'userID' in session:
            session['userID'] = None
        if not 'login' in session:
            session['login'] = False
        response_body = render_template('index.html',
                                        title="メインページ", current_userID=session['userID'], login=session['login'])
        response = prepare_response(response_body)
        return response

    @app.errorhandler(404)
    def page_not_found(error):
        response_body = render_template('page_not_found.html')
        response = prepare_response(response_body)
        return response, 404

    @app.errorhandler(500)
    def internal_server_error(error):
        response_body = render_template('internal_server_error.html')
        response = prepare_response(response_body)
        return response, 500

    from . import auth
    app.register_blueprint(auth.bp)

    from . import quiz
    app.register_blueprint(quiz.bp)

    from . import mypage
    app.register_blueprint(mypage.bp)

    return app
