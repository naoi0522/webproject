# 必要環境変数
SECRET_KEY
PROD_DATABASE_URI

# heroku設定
- heroku configでCLEAR_DATABASE_URLを出力し、そのURLをmysql2にしてから
- heroku config:set DATABASE_URL=""する
- FLASK_APPをquizapp.app.pyに
- mysql+pymysql://に置き換え、reconnect=trueを消したものをPROD_DATABASE_URIに設定する
- SECRET_KEYを設定する
- heroku run flask db upgradeを行う（マイグレーションファイルはローカルで作成したものを使うので注意）
