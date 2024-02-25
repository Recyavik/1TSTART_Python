import math
import random
import turtle
from threading import Thread

class StarrySky:
    def __init__(self):
        turtle.screensize(400, 400, 'DarkSlateBlue')
        turtle.pencolor('white')
        turtle.penup()
        turtle.speed(0)
        turtle.hideturtle()
        for _ in range(30):
            turtle.goto(random.randint(-400, 400), random.randint(-400, 400))
            turtle.dot(3, "white")

class CelestialBody:
    def __init__(self, name, color, x, y, size):
        self.name = name
        self.t = turtle.Turtle()
        self.t.speed(0)
        self.t.pensize(3)
        self.t.color('white')
        self.t.fillcolor(color)
        self.t.shapesize(size)
        self.t.shape('circle')
        self.x = x
        self.y = y
        self.t.penup()
        self.t.goto(self.x, self.y)


    def move(self, radius1, radius2, count, speed=0.01):
        alpha = math.pi * count
        while alpha > math.pi:
            x = math.sin(alpha) * radius1
            y = math.cos(alpha) * radius2
            alpha -= speed / 3
            self.t.goto(int(self.x + x), int(self.y + y))

    def first(self):
        self.move(120, 130, 40, 0.02)

    def second(self):
       self.move(160, 200, 40, 0.015)

    def third(self):
       self.move(280, 240, 40, 0.01)


sky = StarrySky()

s = CelestialBody('Солнце','Gold', 0, 0, 8)

earth = CelestialBody('Земля','DodgerBlue', 0, 20, 3)
venus = CelestialBody('Венера','PeachPuff', 10, -20, 2)
mercury = CelestialBody('Меркурий','Gray', -20, -20, 1)


th1 = Thread(target=mercury.first)
th2 = Thread(target=venus.second)
th3 = Thread(target=earth.third)

th1.start()
th2.start()
th3.start()


turtle.done()

# https://www.youtube.com/watch?v=pm2uUpbJ3T4&t=22s

