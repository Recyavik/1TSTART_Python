import sqlite3
import turtle
db = sqlite3.connect("users")
sql = db.cursor()
sql.execute("""CREATE TABLE IF NOT EXISTS users(
        login TEXT,
        password TEXT
)""")
db.commit()

user_login = input("Логин: ")
user_password = input("Пароль: ")
sql.execute(f"SELECT login FROM users WHERE login='{user_login}'")
if sql.fetchone() is None:
    sql.execute(f"INSERT INTO users VALUES (?, ?)", (user_login, user_password))
    db.commit()
else:
    print("Такой аккаунт уже существует")
    for i in sql.execute("SELECT * FROM users"):
        print(i)


conn = sqlite3.connect("data2.db")
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS data (x REAL, y REAL)""")
t = turtle.Turtle()
conn.commit()

# cur.execute("INSERT INTO data VALUES (?, ?)", (10, 20))
# cur.execute("INSERT INTO data VALUES (?, ?)", (50, 50))
# cur.execute("INSERT INTO data VALUES (?, ?)", (100, -200))
# cur.execute("INSERT INTO data VALUES (?, ?)", (10, 20))
# conn.commit()

cur.execute("SELECT x,y  FROM data")
data = cur.fetchall()
print(data)

com = turtle.Screen()
for x, y in data:
    t.goto(x, y)
    command = com.textinput("Действие", "Далее или Удалить")
    if command.lower() == "далее":
        continue
    elif command.lower() == "удалить":
        cur.execute(f"DELETE FROM data WHERE x = {x}")
        t.undo()
        conn.commit()

while True:
    len = turtle.Screen()
    x = len.numinput("x LEN ", "x", 0, minval=-1, maxval=1000)
    y = len.numinput("y LEN ", "y", 0, minval=-1, maxval=1000)
    if x == -1 or y == -1:
        break
    if x != None and y != None:
        cur.execute("INSERT INTO data VALUES (?, ?)", (x, y))
        conn.commit()
        t.goto(x, y)

turtle.done()
