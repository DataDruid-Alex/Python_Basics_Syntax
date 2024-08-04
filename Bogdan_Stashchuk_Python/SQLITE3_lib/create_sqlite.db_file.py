import sqlite3
DB_NAME = "sqlite_db.db"
with sqlite3.connect(DB_NAME) as sqlite_con:
    print(sqlite_con)
    # print(sqlite3.version)
    print(sqlite3.sqlite_version)
