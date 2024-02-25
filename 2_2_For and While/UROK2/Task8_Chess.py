# Сегодня на практике вложенные циклы for
# Шахматная доска

import turtle as t

w = t.Screen()
w.setup(width=600, height=600)
w.bgcolor("#CCCCFF")
t.speed(0)
x0, y0 = -180, 200
t.pensize(2)
size = 40
color_white = "#FFFFFF"
color_black = "#000000"
t.penup()
t.goto(x0, y0)
t.pendown()
t.begin_fill()
t.color("#A0A0A0", color_white)
for _ in range(4):
    t.forward(size * 8)
    t.right(90)
t.end_fill()
t.color("#A0A0A0", color_black)
flag = True
dx = 0
for y in range(0, size*8, size):
    flag = not flag
    if flag:
        dx = size
    else:
        dx = 0
    for x in range(dx, size *8, size * 2):
        t.begin_fill()
        t.penup()
        t.goto(x0 + x, y0 - y)
        t.pendown()
        for _ in range(4):
            t.forward(size)
            t.right(90)
        t.end_fill()
symbol = "ABCDEFGH"
i = 0
font_size = int(size / 5)
t.pencolor("black")
for x in range(int(size/2), size *8, size):
    t.penup()
    t.goto(x0 + x , y0 + font_size)
    t.pendown()
    t.write(symbol[i], align="center", font=("Arial", font_size, "bold"))
    t.penup()
    t.goto(x0 + x , y0 - font_size * 3 - size * 8)
    t.pendown()
    t.write(symbol[i], align="center", font=("Arial", font_size, "bold"))
    i += 1
i = 1
for y in range(size*8, int(size/2), -size):
    t.penup()
    t.goto(x0 - font_size*2, y0 - y + font_size*2)
    t.pendown()
    t.write(i, align="center", font=("Arial", font_size, "bold"))
    t.penup()
    t.goto(x0 + size*8 + font_size*2, y0 - y + font_size * 2)
    t.pendown()
    t.write(i, align="center", font=("Arial", font_size, "bold"))
    i += 1

t.done()