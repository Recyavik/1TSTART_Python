import turtle

# Создаем шаблон Черепашки
window = turtle.screensize(400, 400, "olive")
t = turtle.Turtle()
t.shape("turtle")
t.pensize(3)
t.speed(10)


turtle.done()

# рисуем линию длиной 100 пикселей
t.pensize(5)
t.color("red")
t.forward(100)

t.right(90)
t.color("orange")
t.backward(50)

t.color("blue")
t.pensize(5)
t.goto(0,0)

# рисуем круг с радиусом 50 пикселей
t.pensize(2)
t.penup()
t.goto(160, 80)
t.pendown()
t.color("green")

t.circle(50)

# выводим текст на экран
t.color("grey")
t.penup()
t.goto(10, -30)
t.write("Hello, Turtle!", font=("Arial", 16, "bold"))

t.color("black")
t.goto(-100, 50)
t.circle(50)


t.color("black")
t.pendown()
t.goto(-100, 50)
t.begin_fill()
t.fillcolor("orange")
t.circle(50)
t.end_fill()

back = turtle.Screen()
back.bgpic("back.png")

# заканчиваем рисование
turtle.done()