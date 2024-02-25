import turtle


def funct():
    pass

x1 = 0

def line(x1, y1, x2, y2):
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.goto(x2, y2)
    t.penup()

t = turtle.Turtle()
t.pensize(3)
line(-100, 10 , 200, 200)
line(100, 10 , -200, 200)
turtle.done()

