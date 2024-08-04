import sqlite3
DB_NAME = "sqlite_db.db"
with sqlite3.connect(DB_NAME) as sqllite_con:
    sql_request = "SELECT * FROM courses WHERE id<=3"
    sql_cursor = sqllite_con.execute(sql_request)
    # for record in sql_cursor:
    #     print(record)
    records = sql_cursor.fetchall()
    print(records)
