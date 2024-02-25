# Сегодня на практике - ЦИКЛ for (алгоритмическая структура перебора последовательности)
# Задача 5. Зебра линий и процедуры библиотеки "turtle"

import turtle



window = turtle.Screen()
window.setup(width=600, height=600)
window.bgcolor('green')

t = turtle.Turtle()
t.speed(0)
x0, y0 = -150, 120


size = step = 10
flag = True
for x in range(0, 300, step):
    flag = not flag
    if flag:
        t.pencolor('gray')
    else:
        t.pencolor('white')
    t.pensize(size)
    t.penup()
    t.goto(x0+x, y0)
    t.pendown()
    t.goto(x0+x, -120)

turtle.done()
