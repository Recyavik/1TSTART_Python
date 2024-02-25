import turtle

class Figure:


    def __init__(self, angle, size=100):
        self.angle = angle
        self.size = size
        self.t = turtle.Turtle()

class Triangle(Figure):

    def __init__(self, angle, size):
        super().__init__(angle=3, size=100)
        self.angle = angle
        self.size = size

    def draw(self):
        for i in range(3):
            turtle.forward(self.size)
            turtle.right(360 / self.angle)


class Square(Figure):

    def __init__(self, angle, size):
        super().__init__(angle=4, size=100)
        self.angle = angle
        self.size = size

    def draw(self):
        for i in range(4):
            turtle.forward(self.size)
            turtle.right(360 / self.angle)

class Circle(Figure):

    def __init__(self, radius):
        self.size = radius

    def draw(self):
        turtle.circle(self.size)


cir1 = Circle(100)
cir2 = Circle(50)

s1 = Square(4, 100)
s2 = Square(4, 50)

t1 = Triangle(3, 100)


list_obj = [cir1, cir2, s1, s2, t1]
for el in list_obj:
    el.draw()

turtle.done()