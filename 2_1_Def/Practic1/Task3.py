import random
import turtle


def polygon_color(number_angle, size):
    turtle.colormode(255)
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0,255)
    t.begin_fill()
    for _ in range(number_angle):
        t.forward(size)
        t.left(360/number_angle)
    t.fillcolor(r, g, b)
    t.end_fill()


t = turtle.Turtle()
t.speed(0)
# polygon_color(6, 100)
# polygon_color(6, 50)
for _ in range(50):
    t.penup()
    x = random.randint(-400, 400)
    y = random.randint(-400, 400)
    size = random.randint(10, 100)
    number_angle = random.randint(3, 8)
    t.goto(x, y)
    # t.left(size)
    t.pendown()
    polygon_color(number_angle, size)


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


draw_house(0,0, 100, 'red')
draw_house(-200,0, 50, 'blue')


turtle.done()