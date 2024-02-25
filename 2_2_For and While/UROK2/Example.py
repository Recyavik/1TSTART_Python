import turtle


w = turtle.Screen()
w.setup(width=500, height=500)
w.bgcolor("#CCCCFF")
t = turtle.Turtle()
t.speed(0)
t.color("#928C8C","#904d30")
t.pensize(2)
size_block = 20
dx = 0
flag = True
x0, y0 = -150, 120
for y in range(30, 240, int(size_block/2)):
    flag = not flag
    if flag:
        dx = size_block / 2
    else:
        dx = 0
    for x in range(0, 300, size_block):
        t.begin_fill()
        t.penup()
        t.goto(x0 + x + dx, y0 - y)
        t.pendown()
        for _ in range(2):
            t.forward(size_block)
            t.right(90)
            t.forward(size_block/2)
            t.right(90)
        t.end_fill()

turtle.done()