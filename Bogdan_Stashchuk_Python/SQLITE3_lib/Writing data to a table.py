import sqlite3
DB_NAME = "sqlite_db.db"
courses = [
    (2, "SQL", 100_000_000, 12_000),
    (3, "Java", 2000, 45),
    (4, "PostgreSQL", 1_000_000, 1000),
    (5, "Tableu", 300_000, 200)
]
with sqlite3.connect(DB_NAME) as sqllite_con:
    sql_request = "INSERT INTO courses VALUES(?,?,?,?)"
    # sqllite_con.execute(sql_request, (1, "Python course", 44, 10))
    for cours in courses:
        sqllite_con.execute(sql_request, cours)
    sqllite_con.commit()
