from flask import *
from DBaccess import *
from QuizManage import *
import mysql.connector

app = Flask(__name__)
dbac = DBaccess()
qmng = QuizManage(dbac)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/post', methods=['GET', 'POST'])
def post():
    if request.method == "POST":
        name = request.form['name']
        return render_template('index.html', name=name)


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    qmng.select_quiz()
    if request.method == "POST":
        ans = request.form['ans']
        return render_template('quiz.html', ans=ans)
    else:
        return render_template('quiz.html')


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
