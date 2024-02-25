# Задача 5. Кирпичная стена
import turtle as t
import time

w = t.Screen()
w.setup(width=500, height=500)
w.bgcolor("green")
t.speed(0)
x0, y0 = -150, 120
# https://www.rapidtables.org/ru/web/color/RGB_Color.html
t.color("#928C8C", "#904d30")
t.pensize(2)
size_block = 40
dx = 0
flag = True
for y in range(30, 240, size_block):
    flag = not flag
    if flag:
        dx = size_block / 2
    else:
        dx = 0
    for x in range(0, 300, size_block):
        t.begin_fill()
        t.penup()
        t.goto(x0 + x + dx, y0 - y / 2)
        t.pendown()
        for _ in range(2):
            t.forward(size_block)
            t.right(90)
            t.forward(size_block / 2)
            t.right(90)
        t.end_fill()
time.sleep(3)
t.down()
