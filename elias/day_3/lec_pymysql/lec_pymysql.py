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




































