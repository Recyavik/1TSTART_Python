import turtle
import random

colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
t = turtle.Turtle()
t.speed(0)
t.width(5)
for _ in range(20):
    t.pencolor(random.choice(colors))
    size = random.randint(10, 100)
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    t.penup()
    t.goto(x, y)
    t.pendown()
    for _ in range(4):
        t.forward(size)
        t.right(90)
turtle.done()

