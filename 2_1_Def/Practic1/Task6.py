import random
import turtle

def draw_house(x, y, size, color):
    t = turtle.Turtle()
    # t.hideturtle()
    # t.speed(0)
    t.pensize(3)
    t.pencolor(color)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.left(60)
    for _ in range(3):
        t.forward(size)
        t.right(360 / 3)
    t.left(30)
    for _ in range(4):
        t.backward(size)
        t.left(90)
    t.penup()
    t.goto(x + size * 5/8, y + size / 4)
    t.pendown()
    t.circle(size/10)
    # t.hideturtle()


draw_house(0,0, 100, 'red')
draw_house(-200,0, 50, 'blue')


turtle.done()