from DBconnect import *


class DBaccess:
    def __init__(self):
        self.conn = DBconnect()

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
