import turtle
import random
import math

scr = turtle.Screen()
scr.screensize(400, 400)
scr.bgcolor("pink")
t = turtle.Turtle()
scr.title("Ромашка")
t.speed(0)
t.pensize(2)
t.penup()
t.goto(-300, 300)
t.pendown()
t.write("Реши правильно пример и получи ромашку!", font=("Helvetica", 16, "normal"))
value1 = random.randint(0, 20)
value2 = random.randint(0, 20)
if value1 < value2:
    value1, value2 = value2, value1
operation = random.randint(0, 4)
if operation == 0:
    answer = value1 + value2
    example = f"{value1} + {value2} = "
elif operation == 1:
    answer = value1 - value2
    example = f"{value1} - {value2} = "
elif operation == 1:
    answer = value1 - value2
    example = f"{value1} * {value2} = "
else:
    # 5 * 4 = 20, 20 : 4 = 5
    answer = value1 * value2
    answer, value2 = value2, answer
    example = f"{value2} : {value1} = "

answer_user = scr.textinput("Реши пример:", example)
if answer_user.isdigit():
    answer_user = int(answer_user)
    if answer_user == answer:
        t.penup()
        t.goto(-300, 200)
        t.pendown()
        t.pencolor("green")
        t.write("Молодец, правильно!   " + example + str(answer), font=("Helvetica", 18, "bold"))
        radius = 30

        t.pencolor("black")
        t.penup()
        alpha = math.radians(0)
        x = math.sin(alpha) * radius
        y = (1 - math.cos(alpha)) * radius
        t.goto(x, y - 30)
        t.pendown()
        t.begin_fill()
        t.fillcolor("white")
        t.circle(radius*1.5)
        t.end_fill()

        t.penup()
        alpha = math.radians(120)
        x = math.sin(alpha) * radius
        y = (1 - math.cos(alpha)) * radius
        t.goto(x, y - 30)
        t.pendown()
        t.begin_fill()
        t.fillcolor("white")
        t.circle(radius*1.5)
        t.end_fill()

        t.penup()
        alpha = math.radians(240)
        x = math.sin(alpha) * radius
        y = (1 - math.cos(alpha)) * radius
        t.goto(x, y - 30)
        t.pendown()
        t.begin_fill()
        t.fillcolor("white")
        t.circle(radius*1.5)
        t.end_fill()

        t.penup()
        t.goto(0, 0)
        t.pendown()
        t.begin_fill()
        t.fillcolor("yellow")
        t.circle(radius)
        t.end_fill()

        turtle.done()
    else:
        t.pencolor("red")
        t.penup()
        t.goto(-300, 200)
        t.pendown()
        t.write("Неверный ответ, потому что вы указали, что " + example + str(answer_user),
                font=("Helvetica", 16, "normal"))
        t.penup()
        t.pencolor("black")
        t.goto(-300, 150)
        t.pendown()
        t.write("Пожалуйста запомните, что " + example + str(answer), font=("Helvetica", 18, "bold"))
else:
    t.penup()
    t.goto(-300, 100)
    t.pendown()
    t.color("red")
    t.write("Ошибка ввода", font=("Helvetica", 18, "bold"))
turtle.done()
