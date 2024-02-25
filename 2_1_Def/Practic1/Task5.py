import math
import turtle


def ellipse(x, y, r1, r2):
    t.penup()
    x = x + r1
    cx0 =r1 * math.cos(- math.pi) + x
    cy0 = r2 * math.sin(- math.pi) + y
    t.goto(cx0 - r1, cy0)
    t.pendown()
    alpha = - math.pi
    while alpha <= math.pi:
        cx = r1 * math.cos(alpha) + x
        cy = r2 * math.sin(alpha) + y
        t.goto(cx - r1, cy)
        alpha += 0.1
    t.penup()
    t.goto(x - 2 * r1, y)
    t.pendown()


def line(x1, y1, x2, y2):
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.goto(x2, y2)
    t.penup()

def cylinder(x, y, r1, r2, h):
    ellipse(x, y, r1, r2)
    line(x + r1, y, x + r1, y + h)
    ellipse(x, y + h, r1, r2)
    line(x - r1, y, x - r1, y + h)

t = turtle.Turtle()
t.pensize(3)
cylinder(0,0,75, 25, 200)
cylinder(-300,0,50, 25, 100)
# ellipse(0,0, 75, 25)
# line(75,0, 75, 200)
# ellipse(0,200, 75, 25)
# line(-75,0, -75, 200)
turtle.done()