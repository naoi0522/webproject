from flask import *
from database import init_db
from models.quiz import Quiz
from models.user import User
import config

app = Flask(__name__)
app.config.from_object('config.Config')
init_db(app)


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


@app.route('/addquiz', methods=['GET', 'POST'])
def addquiz():
    if request.method == "POST":
        problem = request.form['problem']
        correct = request.form['correct']
        return render_template('addquiz.html')
    else:
        return render_template('addquiz.html')


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
