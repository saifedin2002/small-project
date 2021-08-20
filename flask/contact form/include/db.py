import sqlite3
db = sqlite3.connect("include/flask.db", check_same_thread=False)
cr = db.cursor()
cr.execute("CREATE TABLE IF NOT exists users ( name text, email text , password text  ) ")