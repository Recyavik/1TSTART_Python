import turtle
import sqlite3

class PenPlay:

    def __init__(self):
        self.pen_status = False
        self.pen_size = 3
        self.pen_color = "black"
        self.x = 0
        self.y = 0
        self.init_turtle()

    def init_turtle(self):
        self.wn = turtle.Screen()
        self.wn.title("Графический редактор")
        self.wn.setup(800, 600)
        self.wn.getcanvas().config(cursor="arrow")
        # wn.tracer(0)

        pensize = 1
        self.pen = turtle.Turtle()
        self.pen.pencolor('black')
        self.pen.penup()
        self.pen.shapesize(pensize / 3)
        self.pen.pencolor('black')

        self.conn = sqlite3.connect('turtle.db')
        self.cursor = self.conn.cursor()

    def read_record(self):
        self.cursor.execute("SELECT * FROM cor")
        self.rows = self.cursor.fetchall()
        for row in self.rows:
            print(row)
        self.conn.close()

    def pen_draw(self):
        self.pen.penup()
        for row in self.rows:
            row_list = list(row)
            self.pen_status = row_list[1]
            self.pen_size = row_list[2]
            self.pen_color = row_list[3]
            self.x = row_list[4]
            self.y = row_list[5]
            if self.pen_status == 1:
                self.pen.penup()
            elif self.pen_status == 0:
                self.pen.pendown()
            self.pen.pensize(self.pen_size)
            self.pen.pencolor(self.pen_color)
            self.pen.goto(self.x, self.y)
            # self.wn.update()

pero = PenPlay()
pero.read_record()
pero.pen_draw()
turtle.done()