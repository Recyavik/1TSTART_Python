# Рисуем колесо со спицами по формуле единичной окружности
import math
import turtle as t

w = t.screensize(400, 400, bg="gray")
t.speed(0)
t.pensize(1)
radius = 200
x0 = 0
y0 = 0
t.pensize(2)
t.penup()
t.goto(x0, y0)
t.pendown()
flag = True
alpha = 0
step = 2 * math.pi / 30
while alpha < math.pi * 2:
    if flag:
        t.pencolor("white")
    else:
        t.pencolor("blue")
    flag = not (flag)
    x = (math.sin(alpha) * radius)
    y = (math.cos(alpha) * radius)
    t.goto(x + x0, y + y0)
    t.goto(x0, y0)
    alpha += step
t.penup()
t.pensize(15)
t.goto(x0, y0 - radius)
t.pendown()
t.pencolor("black")
t.circle(radius)
t.penup()
t.done()