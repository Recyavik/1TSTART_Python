import math
import turtle

class Hero:
    x_default = 0
    y_default = 0
    size_default = 10
    color = 'black'
    t = turtle.Turtle()

    def __init__(self, x=x_default, y=y_default, size=size_default):
        self.x = x
        self.y = y
        self.size = size
        self.set_position(self.x, self.y)

    def set_position(self, x, y):
        self.t.heading()
        self.t.penup()
        self.t.speed('fastest')
        self.t.pensize(3)
        self.t.pencolor('black')
        self.t.penup()
        self.t.goto(self.x, self.y)
        self.t.pendown()

    def draw_wheel(self, x0=0, y0=0):
        self.t.pensize(1)
        radius = self.size / 4
        self.t.pensize(2)
        self.t.penup()
        self.t.goto(x0, y0)
        self.t.pendown()
        flag = True
        alpha = 0
        step = 2 * math.pi / 30
        while alpha < math.pi * 2:
            if flag:
                self.t.pencolor("white")
            else:
                self.t.pencolor("blue")
            flag = not (flag)
            x = (math.sin(alpha) * radius)
            y = (math.cos(alpha) * radius)
            self.t.goto(x + x0, y + y0)
            self.t.goto(x0, y0)
            alpha += step
        self.t.penup()
        self.t.pensize(int(self.size/10))
        self.t.goto(x0, y0 - radius)
        self.t.pendown()
        self.t.pencolor("black")
        self.t.circle(radius)
        self.t.penup()

    def draw_house(self, color):
        self.t.heading()
        # t.hideturtle()
        # t.speed(0)
        self.t.begin_fill()
        self.t.left(60)
        for _ in range(3):
            self.t.forward(self.size)
            self.t.right(360 / 3)
        self.t.left(30)
        for _ in range(4):
            self.t.backward(self.size)
            self.t.left(90)
        self.t.penup()
        self.t.goto(self.x + self.size * 5/8, self.y + self.size / 4)
        self.t.pendown()
        self.t.circle(self.size/10)
        self.t.fillcolor(color)
        self.t.end_fill()
        self.t.heading()
        # t.hideturtle()

    def draw_car(self, color):
        self.t.begin_fill()
        self.t.left(90)
        self.t.forward(self.size/3)
        self.t.right(80)
        self.t.forward(self.size)
        self.t.left(35)
        self.t.forward(self.size / 2)
        self.t.right(45)
        self.t.forward(self.size)
        self.t.right(45)
        self.t.forward(self.size / 2)
        self.t.right(45)
        self.t.forward(self.size / 2)
        self.t.left(90)
        self.t.backward(self.size * 2.7)
        self.t.goto(self.x, self.y)
        self.t.fillcolor(color)
        self.t.end_fill()
        self.t.penup()
        self.t.begin_fill()
        self.t.forward(self.size)
        self.t.left(90)
        self.t.forward(self.size / 2)
        self.t.right(90)
        self.t.pendown()

        self.t.begin_fill()
        self.t.pencolor('skyblue')
        self.t.left(45)
        self.t.forward(self.size / 2)
        self.t.right(45)
        self.t.forward(self.size - 3)
        self.t.right(45)
        self.t.forward(self.size / 2)
        self.t.left(45)
        self.t.backward(self.size * 2 - self.size / 4)
        self.t.fillcolor('skyblue')
        self.t.end_fill()
        self.t.hideturtle()

        self.draw_wheel(self.x + int(self.size/2), self.y)
        self.draw_wheel(self.x + int(self.size *2.2), self.y)
        self.t.penup()
        self.t.goto(self.x, self.y)

    def draw_tree(self, size, level):
        self.t.speed('fastest')
        angle = 30
        if level > 0:
            self.t.screen.colormode(255)
            self.t.pencolor(0, 255 // level, 0)
            self.t.forward(size)
            self.t.right(angle)
            self.draw_tree(0.8 * size, level - 1)
            self.t.pencolor(0, 255 // level, 0)
            self.t.left(2 * angle)
            self.draw_tree(0.8 * size, level - 1)
            self.t.pencolor(0, 255 // level, 0)
            self.t.right(angle)
            self.t.forward(-size)

obj_car = Hero(0, -200, 50)
obj_car.draw_car('red')

obj_car2 = Hero(-200, 200, 100)
obj_car2.draw_car('blue')


obj_house1 = Hero(200, 200, 80)
obj_house1.draw_house('gray')


obj_tree = Hero(-200, -200, 40)
obj_tree.draw_tree(80, 7)
#
turtle.done()