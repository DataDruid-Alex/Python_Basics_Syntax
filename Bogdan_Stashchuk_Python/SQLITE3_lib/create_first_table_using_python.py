import sqlite3
DB_NAME = "sqlite_db.db"
with sqlite3.connect(DB_NAME) as sqlite_con:
    sql_request = """CREATE TABLE IF NOT EXISTS courses(
    id integer PRIMARY KEY,
    title text NOT NULL,
    students_qnt integer,
    reviews_qnt integer
    );"""
    sqlite_con.execute(sql_request)
