from flask import *
from database import init_db
from models.quiz import Quiz
from models.user import User
from quizmanage import *
import config

app = Flask(__name__)
app.config.from_object('config.Config')
init_db(app)
qmng = QuizManage()


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == "POST":
        ans = request.form['ans']
        return render_template('quiz.html', ans=ans)
    else:
        return render_template('quiz.html')


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


if __name__ == '__main__':
    app.debug = True
    app.run()
