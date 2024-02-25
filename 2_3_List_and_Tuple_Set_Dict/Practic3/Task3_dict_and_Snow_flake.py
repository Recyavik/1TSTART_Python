# Все случайные координаты запомнить как словарь координат, добавить к словарю список цветов
# Используя полученный словарь нарисовать цветные снежинки
import random
import turtle
import random as rnd


rnd.seed()
cor_and_color = dict()
for _ in range(0, 30):
    x = rnd.randint(-300, 300)
    y = rnd.randint(-300, 300)
    cor_and_color[x] = y
print(cor_and_color)
print(len(cor_and_color))
cor_and_color['color'] = ['Teal', 'LightSeaGreen', 'RoyalBlue', 'DodgerBlue', 'DeepSkyBlue', 'LightSkyBlue',
                        'Snow', 'Cyan', 'LightCyan', 'White', 'Aquamarine', 'Aqua', 'Fuchsia', 'LavenderBlush']
print(cor_and_color)
print(len(cor_and_color))

t = turtle.Turtle()
t.screen.screensize(400, 400, bg='black')
t.speed(0)
t.pensize(2)
for key in cor_and_color.keys():
    color = random.choice(cor_and_color['color'])
    t.pencolor(color)
    size = rnd.randint(10,30)
    t.penup()
    t.goto(key, cor_and_color[key])
    t.pendown()
    for i in range(6):
        t.forward(size)
        for j in range(2):
            t.backward(size/2)
            t.left(30)
            t.forward(size/2)
            t.backward(size/2)
            t.right(60)
            t.forward(size/2)
            t.backward(size/2)
            t.left(30)
        t.left(360/6)
turtle.done()