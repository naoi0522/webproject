from flask import *
import os
app = Flask(__name__)


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
    if request.method == "POST":
        ans = request.form['ans']
        return render_template('quiz.html', ans=ans)


if __name__ == '__main__':
    port = int(os.getenv("PORT"))
    app.run(host="0.0.0.0", port=port)
