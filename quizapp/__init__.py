from flask import *
from quizapp.database import init_db
import quizapp.models
from quizapp.quizmanage import *
import quizapp.config

#app = Flask(__name__)
qmng = QuizManage()


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('quizapp.config.Config')
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

    init_db(app)

    @app.route('/', methods=['GET', 'POST'])
    def index():
        qmng.new_quiz()
        if not 'userID' in session:
            session['userID'] = None
        return render_template('index.html',
                               title="メインページ", current_userID=session['userID'])
# TODO quizのblueprint化

    @app.route('/quiz', methods=['GET', 'POST'])
    def quiz():
        if request.method == "POST":
            ans = request.form['ans']
            result, quiz_num, problem = qmng.judge(ans)
            return render_template('quiz.html',
                                   title="クイズ", current_userID=session['userID'], answered=True,
                                   quiz_num=quiz_num, problem=problem, ans=ans, result=result)
        else:
            quiz_num, problem = qmng.get_next_quiz()
            return render_template('quiz.html',
                                   title="クイズ", current_userID=session['userID'], answered=False,
                                   quiz_num=quiz_num, problem=problem)

    @app.route('/result', methods=['GET'])
    def result():
        total = qmng.get_correct_total()
        return render_template('result.html',
                               title="結果発表", current_userID=session['userID'], total=total)

    @app.route('/registerquiz', methods=['GET', 'POST'])
    def registerquiz():
        if request.method == "POST":
            problem = request.form['problem']
            correct = int(request.form['correct'])
            userID = session['userID']

            qmng.register_quiz(problem, correct, userID)

            # TODO 入力値の制限(空白など),登録可否での処理の変更

            return render_template('registerquiz.html',
                                   title="クイズ登録", current_userID=session['userID'])
        else:
            return render_template('registerquiz.html',
                                   title="クイズ登録", current_userID=session['userID'])

    from . import auth
    app.register_blueprint(auth.bp)

    return app
