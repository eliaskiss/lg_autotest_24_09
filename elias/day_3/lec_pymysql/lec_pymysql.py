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

    ################################################################
    # Execute Only
    ################################################################
    def execute_only(self, sql, values=None):
        try:
            # select * from elias;
            # select * from elias where name = "kim" and age = 20;
            # name = "kim"
            # age = 20
            # sql = 'select * from elias where name = %s, and age = %s;'
            # values = (name, age)
            if self.conn is not None:
                if values is None:
                    self.cursor.execute(sql)
                else:
                    self.cursor.execute(sql, values)
        except Exception as e:
            message = f'--> Exception is {e} (Line: {sys.exc_info()[-1].tb_lineno})'
            ic(message)





if __name__ == '__main__':
    db = Database(host='139.150.73.242', user='dbuser', passwd='dbuser', db='lg_autotest')
    db.connect_db()



































