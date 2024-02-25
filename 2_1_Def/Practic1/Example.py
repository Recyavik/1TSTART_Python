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



def polygon(n):
    for _ in range(n):
        t.forward(100)
        t.left(360/n)


sc = turtle.Screen()
sc.setup(600, 600)
t = turtle.Turtle()
while True:
    cmd = turtle.textinput('Окно управления черепахой', 'Введите команду')
    if cmd == 'выход' or cmd == 'прервать':
        break
    elif cmd == 'шестиугольник':
        polygon(6)
    elif cmd == 'треугольник':
        polygon(3)
    elif cmd == 'квадрат':
        polygon(4)
    elif cmd == 'круг':
        t.circle(100)
    elif cmd == 'дом':
        draw_house(-200, -100, 50, 'blue')

turtle.done()