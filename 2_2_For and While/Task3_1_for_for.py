# Вложенные циклы
import random
import turtle
# turtle.speed(0)
turtle.pensize(3)
turtle.penup()
turtle.goto(0, 200)
turtle.pendown()
turtle.colormode(255)
for j in range(14): # 0,1,2,3,4,5,6,7,8,9,10,11,12,13 - всего 14
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    turtle.pencolor(r, g, b)
    for i in range(4): # внутренний цикл
        turtle.forward(40)
        turtle.right(90)
    turtle.left(25)
    turtle.backward(60)

turtle.done()