import pymysql
from icecream import ic
import sys

ic.configureOutput(includeContext=True)
# ic.disable()

# SQL Tutorial
# https://www.w3schools.com/sql/sql_where.asp
# https://www.tutorialspoint.com/sql/sql-create-table.htm

class Database:
    def __init__(self, host, user, passwd, db):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db

        self.cursor = None  # Cursor 객체
        self.conn = None    # Connection 객체

    ################################################################
    # Connect DB
    ################################################################
    def connect_db(self):
        try:
            if self.conn is None:
                self.conn = pymysql.connect(host=self.host,
                                            user=self.user,
                                            password=self.passwd,
                                            db=self.db)
                self.cursor = self.conn.cursor()    # row[0], row[1], row[2], ...
                self.cursor = self.conn.cursor(pymysql.cursors.DictCursor) # row['id'], row['reg_datetime'], row['name'], ...

            ic('DB is connected')
        except Exception as e:
            message = f'--> Exception is {e} (Line: {sys.exc_info()[-1].tb_lineno})'
            ic(message)





































