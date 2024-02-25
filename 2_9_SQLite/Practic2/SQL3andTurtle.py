import sqlite3
import turtle

db = sqlite3.connect("data.db")
sql = db.cursor()
sql.execute("""CREATE TABLE IF NOT EXISTS data(
        x REAL,
        y REAL
)""")
db.commit()

sql.execute(f"INSERT INTO data VALUES (?, ?)", (10, 20))
sql.execute(f"INSERT INTO data VALUES (?, ?)", (20, 100))
sql.execute(f"INSERT INTO data VALUES (?, ?)", (130, 150))
db.commit()

sql.execute("SELECT * FROM data")
data = sql.fetchall()

turtle.color("red")
turtle.pensize(3)
for x, y in data:
    turtle.goto(x, y)

turtle.done()
