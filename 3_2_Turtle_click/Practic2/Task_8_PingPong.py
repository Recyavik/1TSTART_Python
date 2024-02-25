import turtle

# Создание окна игры
wn = turtle.Screen()
wn.title("Пинг-понг")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Создание ракетки игрока 1
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=6, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Создание ракетки игрока 2
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=6, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Создание мяча
ball = turtle.Turtle()
ball.speed(40)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = -0.2  # type: ignore


# Функции управления ракетками
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:
        y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    if y > -240:
        y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:
        y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    if y > -240:
        y -= 20
    paddle_b.sety(y)


# Установка клавиш управления
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Основной игровой цикл
while True:
    wn.update()

    # Перемещение мяча
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Проверка на столкновение с верхней и нижней стенами
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1

    # Проверка на столкновение с ракетками
    if (ball.dx > 0) and (350 > ball.xcor() > 340) and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
        ball.color("blue")
        ball.setx(340)
        ball.dx *= -1

    elif (ball.dx < 0) and (-350 < ball.xcor() < -340) and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
        ball.color("red")
        ball.setx(-340)
        ball.dx *= -1

    # Проверка на выигрыш
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
