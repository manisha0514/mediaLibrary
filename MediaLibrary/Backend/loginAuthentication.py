import os
import sqlite3

def login_check(userName, password):
    db_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    connection = sqlite3.connect(db_dir + r"\Database\mediaLibrary.sqlite")
    result = connection.execute("SELECT * FROM usertable WHERE userId = ? AND password = ?", (userName, password))
    if result.fetchall():
        return True
    else:
        print("invalid login")
        return False
