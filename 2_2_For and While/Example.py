import math
import turtle
import turtle as t

w = t.screensize(400, 400, bg="gray")
t.speed(0)
t.pensize(2)
radius = 200
x0, y0 = 0, 0
t.goto(x0, y0)
t.pendown()
flag = True
step = 2 * math.pi / 60
alpha = 0
while alpha < math.pi * 2:
    if flag:
        t.pencolor("white")
    else:
        t.pencolor("blue")
    flag = not flag
    x = math.sin(alpha) * radius
    y = math.cos(alpha) * radius
    t.goto(x0 + x, y0 +y)
    t.goto(x0, y0)
    alpha = alpha + step
t.penup()
t.pensize(15)
t.goto(x0, y0 - radius)
t.pendown()
t.pencolor("black")
t.circle(radius)
t.penup()

turtle.done()

