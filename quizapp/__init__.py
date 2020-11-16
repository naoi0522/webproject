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

    init_db(app)

    @app.route('/', methods=['GET', 'POST'])
    def index():
        qmng.new_quiz()
        return render_template('index.html')

    @app.route('/quiz', methods=['GET', 'POST'])
    def quiz():
        if request.method == "POST":
            ans = request.form['ans']
            result, quiz_num, problem = qmng.judge(ans)
            return render_template('quiz.html', answered=True, quiz_num=quiz_num, problem=problem, ans=ans, result=result)
        else:
            quiz_num, problem = qmng.get_next_quiz()
            return render_template('quiz.html', answered=False, quiz_num=quiz_num, problem=problem)

    @app.route('/result', methods=['GET'])
    def result():
        total = qmng.get_correct_total()
        return render_template('result.html', total=total)

    @app.route('/registerquiz', methods=['GET', 'POST'])
    def registerquiz():
        if request.method == "POST":
            problem = request.form['problem']
            correct = int(request.form['correct'])

            qmng.register_quiz(problem, correct)

            return render_template('registerquiz.html')
        else:
            return render_template('registerquiz.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == "POST":
            userID = request.form['userID']
            passwd = request.form['passwd']

            return render_template('login.html', userID=userID, passwd=passwd)
        else:
            return render_template('login.html')

    return app
