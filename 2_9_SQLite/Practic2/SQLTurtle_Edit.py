import turtle
import sqlite3

class Pen:

    def __init__(self):
        self.pen_status = True
        self.pen_size = 1
        self.pen_color = "black"
        self.x = 0
        self.y = 0
        self.init_turtle()

    def init_turtle(self):
        self.wn = turtle.Screen()
        self.wn.title("Графический редактор")
        self.wn.setup(800, 600)
        self.wn.getcanvas().config(cursor="arrow")
        self.wn.tracer(0)

        pensize = 1
        self.pen = turtle.Turtle()
        self.pen.pencolor('black')
        self.pen.penup()
        self.pen.shapesize(pensize / 3)
        self.pen.hideturtle()
        print("log: Перо поднято")

        self.conn = sqlite3.connect('turtle.db')
        self.cursor = self.conn.cursor()

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS cor (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pen INTEGER,
            size INTEGER,
            color TEXT,
            x INTEGER,
            y INTEGER);
            """)
        self.conn.commit()

    def add_record(self):
        self.cursor.execute("INSERT INTO cor (pen, size, color, x, y) VALUES (?, ?, ?, ?, ?)",
                   (int(self.pen_status), self.pen_size, self.pen_color, self.x, self.y))
        self.conn.commit()

    def change_color_red(self):
        self.pen.pencolor('red')
        print("log: Установлен цвет пера красный")
        self.pen_color = 'red'
        self.add_record()

    def change_color_green(self):
        self.pen.pencolor('green')
        print("log: Установлен цвет пера зеленый")
        self.pen_color = 'green'
        self.add_record()

    def change_color_blue(self):
        self.pen.pencolor('blue')
        print("log: Установлен цвет пера синий")
        self.pen_color = 'blue'
        self.add_record()

    def pen_up_down(self, x, y):

        if self.pen_status == 0:
            self.pen.penup()
            self.pen.hideturtle()
            print("log: Перо поднято")
        else:
            self.pen.showturtle()
            self.pen.goto(x, y)
            self.pen.pendown()
            print("log: Перо опущено")
        self.add_record()
        self.pen_status = not self.pen_status


    def draw_line(self, x, y):
        print(f"log: Перо в координатах: ({x}, {y})")
        self.pen.goto(x, y)
        self.x = x
        self.y = y
        self.add_record()

    def change_size_pen_inc(self):
        if self.pen_size < 10:
            self.pen_size += 1
        self.pen.pensize(self.pen_size)
        self.pen.shapesize(self.pen_size/3)
        print("log: Увеличили толщину пера")
        self.add_record()

    def change_size_pen_dec(self):
        if self.pen_size > 2:
            self.pen_size -= 1
        self.pen.pensize(self.pen_size)
        self.pen.shapesize(self.pen_size/3)
        print("log: Уменьшили толщину пера")
        self.add_record()

    def quit_edit(self):
        self.pen.clear()
        self.wn.bye()
        self.conn.close()


pero = Pen()

while True:


    pero.wn.update()

    pero.wn.listen()
    pero.wn.onscreenclick(pero.draw_line, btn=1)
    pero.wn.onscreenclick(pero.pen_up_down, btn=3)

    pero.wn.onkey(pero.change_size_pen_inc, '+')
    pero.wn.onkey(pero.change_size_pen_dec, '-')

    pero.wn.onkey(pero.change_color_red, 'r')
    pero.wn.onkey(pero.change_color_red, 'R')

    pero.wn.onkey(pero.change_color_green, 'g')
    pero.wn.onkey(pero.change_color_green, 'G')

    pero.wn.onkey(pero.change_color_blue, 'b')
    pero.wn.onkey(pero.change_color_blue, 'B')

    pero.wn.onkey(pero.quit_edit, 'q')
    pero.wn.onkey(pero.quit_edit, 'Q')