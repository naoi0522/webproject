from DBconnect import *


class DBaccess:
    def __init__(self):
        self.conn = DBconnect()

    def quiz_count(self):
        self.cur = self.conn.connect()

        sql = "SELECT COUNT(*) FROM quiz"
        self.cur.execute(sql)
        rows = self.cur.fetchall()

        self.conn.close()

        return rows[0][0]

    def select(self):
        self.cur = self.conn.connect()

        self.sql = "SELECT * FROM quiz"
        self.cur.execute(self.sql)
        self.rows = self.cur.fetchall()

        self.conn.close()

        return self.rows

    def insert(self):
        self.cur = self.conn.connect()

        self.sql = ""
        self.cur.execute(self.sql)

        self.conn.close()

    def update(self):
        self.cur = self.conn.connect()

        self.sql = ""
        self.cur.execute(self.sql)

        self.conn.close()

    def delete(self):
        self.cur = self.conn.connect()

        self.sql = ""
        self.cur.execute(self.sql)

        self.conn.close()
