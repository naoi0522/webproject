from flask import *
from quizapp.database import init_db
import quizapp.models
import quizapp.config
from flask_graphql import GraphQLView
from flask_graphql_auth import GraphQLAuth
from flask_cors import CORS


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('quizapp.config.Config')
    app.config["JSON_AS_ASCII"] = False
    app.config['SECRET_KEY'] = "PS4"
    app.config["JWT_SECRET_KEY"] = "SWITCH"
    auth = GraphQLAuth(app)
    CORS(app)
    init_db(app)

    from quizapp.schema.schema import schema

    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view(
            'graphql',
            schema=schema,
            graphiql=True
        )
    )

    @app.route("/graphql", methods=["GET"])
    def playground_render():
        return app.send_static_file('playground.html')

    # @app.route('/', methods=['GET'])
    # def index():
    #     if not 'userID' in session:
    #         session['userID'] = None
    #     if not 'login' in session:
    #         session['login'] = False

    #     login_status = bjson.build_login_status(
    #         session['userID'], session['login'])

    #     # return jsonify(login_status)

    #     return render_template('index.html',
    #                            title="メインページ", current_userID=session['userID'], login=session['login'])

    # from . import auth
    # app.register_blueprint(auth.bp)

    # from . import quiz
    # app.register_blueprint(quiz.bp)

    # from . import mypage
    # app.register_blueprint(mypage.bp)

    return app
