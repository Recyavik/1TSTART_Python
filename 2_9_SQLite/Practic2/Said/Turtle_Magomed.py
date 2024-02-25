import turtle
import sqlite3

db = sqlite3.connect("cor_turtle.db")
cur = db.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS turtle1(
        x REAL,
        y REAL,
        color TEXT,
        pensize INT
)""")

# cur.execute('''DROP TABLE IF EXISTS turtle1''')
# cur.execute("INSERT INTO turtle1 VALUES (?,?,?,?)",(50,100,"red",5))
# cur.execute("INSERT INTO turtle1 VALUES (?,?,?,?)",(200,200,"green",10))
# cur.execute("INSERT INTO turtle1 VALUES (?,?,?,?)",(150,300,"blue",8))


db.commit()
#
cur.execute("SELECT * FROM turtle1")
rows = cur.fetchall()
print(rows)
print(rows[0][2])
t = turtle.Turtle()
win = turtle.Screen()
i=0
while(True):
    que = win.textinput("Выбор действия","Далее, назад, обновить, удалить")
    if(que.lower()=="далее"):
        t.pencolor(rows[i][2])
        t.pensize(rows[i][3])
        t.goto(rows[i][0],rows[i][1])
        i+=1
    elif(que.lower()=='назад'):
        i-=1
        t.undo()
    elif(que.lower()=="обновить"):
        i-=1
        que = win.textinput("Выбор действия","что вы хотите обновить x, y, цвет, размер линии")
        if(que.lower()=='x'):
            x = win.numinput("Действие","Введите x")
            cur.execute("UPDATE turtle1 SET x = ? WHERE x=?",(x,rows[i][0]))
            t.undo()
            rows[i]=(x,rows[i][1],rows[i][2],rows[i][3])
            t.pencolor(rows[i][2])
            t.pensize(rows[i][3])
            t.goto(rows[i][0], rows[i][1])
            db.commit()
        if (que.lower() == 'y'):
            y = win.numinput("Действие", "Введите y")
            cur.execute("UPDATE turtle1 SET y = ? WHERE x=?", (y, rows[i - 1][0]))
            t.undo()
            rows[i] = (rows[i][0],y,rows[i][2],rows[i][3])
            t.goto(rows[i])
            db.commit()
        i+=1
    elif(que.lower()=='удалить'):
        cur.execute("DELETE FROM turtle1 WHERE x=?",(rows[i-1][0],))
        rows.pop(i-1)
        t.undo()
        i-=1
        db.commit()
    if(len(rows)==i):
        break
#
while(True):
    que = win.textinput("Выбор действия", "Добавить либо выход")
    if(que.lower()=="добавить"):
        x = win.numinput("Координаты","Напишите координату x")
        y = win.numinput("Координаты","Напишите координату y")
        color = win.textinput("Цвет","Введите цвет")
        size = win.numinput("Размер линии","Введите размер линии")
        cur.execute("INSERT INTO turtle1 VALUES (?,?,?,?)",(x,y,color,size))
        db.commit()
        t.pencolor(color)
        t.pensize(size)
        t.goto(x,y)
    elif(que.lower()=="выход"):
        break

turtle.done()