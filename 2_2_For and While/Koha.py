import turtle as t
import  random as rnd
# Рисунок
w = t.Screen()
w.setup(width=600, height=480)
w.bgcolor('white')
t.speed(0)
size = 300
n = 2
x, y = -150, 50
t.penup()
t.goto(x, y)
t.pendown()
t.pensize(2)
r = rnd.random()
g = rnd.random()
b = rnd.random()
t.pencolor(r, g, b)

def Koch(size,n):
    if n == 0:
        t.forward(size)
    else:
        Koch(size/3, n-1)
        t.left(60)
        Koch(size / 3, n - 1)
        t.right(120)
        Koch(size / 3, n - 1)
        t.left(60)
        Koch(size / 3, n - 1)

def Draw_Koch_Snow(size, n):
    for i in range (3):
        Koch(size, n)
        t.right(120)

count = int(input('Сколько снежинок хотите нарисовать:'))
for i in range(count):
    r = rnd.random()
    g = rnd.random()
    b = rnd.random()
    t.pencolor(r, g, b)
    x, y = -int(rnd.randint(10,100)), int(rnd.randint(10,50))
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.pensize(2)
    size = int(rnd.randint(30,300))
    t.right(int(rnd.randint(0,360)))
    Draw_Koch_Snow(size, n)
t.done()
