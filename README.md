# Usage

`pip install -r requirements.txt`

## windows
`set FLASK_APP=quizapp/wsgi.py`

## Mac/Linux
`export FLASK_APP=quizapp.wsgi.py`

### Develop環境
`flask run`

# heroku設定
- heroku configでCLEAR_DATABASE_URLを出力し、出力したURLのmysqlをmysql2にして
- heroku config:set DATABASE_URL=""する
- FLASK_APPをquizapp.app.pyに
- mysql+pymysql://に置き換え、reconnect=trueを消したものをPROD_DATABASE_URIに設定する
- SECRET_KEYを設定する
- heroku run flask db upgradeを行う（マイグレーションファイルはローカルで作成したものを使うので注意）
