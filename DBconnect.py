import mysql.connector


class DBconnect:
    def connect(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            port='3306',
            user='root',
            password='tbctbctbc',
            database='webquizapp'
        )
        self.cur = self.conn.cursor()
        return self.cur

    def close(self):
        self.cur.close()
        self.conn.close()
