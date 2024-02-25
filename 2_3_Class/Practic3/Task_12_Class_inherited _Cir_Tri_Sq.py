import turtle


class Figures:

    def __init__(self, x0=0, y0=0, size=10, color_base="black"):
        self.__color = color_base
        self.__x0 = x0
        self.__y0 = y0
        self.__size = size

    @property
    def x0(self):
        return self.__x0

    @x0.setter
    def x0(self, x):
        self.__x0 = x

    @property
    def y0(self):
        return self.__y0

    @y0.setter
    def y0(self, y):
        self.__y0 = y

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, c):
        self.__color = c

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, side):
        self.__size = side

    @classmethod
    def draw(cls):
        f = turtle.Turtle()
        f.speed(0)
        f.pensize(3)
        f.penup()
        f.begin_fill()
        return f

class FigureCircle(Figures):

    def __init__(self, x=0, y=0, radius=10, color="black", fill_color="red"):
        super().__init__()
        self.color = color
        self.x0 = x
        self.y0 = y
        self.size = radius
        self.fill = fill_color

    def draw(self):
        f = super().draw()
        f.setposition(self.x0, self.y0)
        f.pendown()
        f.pencolor(self.color)
        f.fillcolor(self.fill)
        f.circle(self.size)
        f.end_fill()


class FigureSquare(Figures):

    def __init__(self, x=0, y=0, side=10, color="black", fill_color="red"):
        super().__init__()
        self.color = color
        self.x0 = x
        self.y0 = y
        self.size = side
        self.fill = fill_color

    def draw(self):
        f = super().draw()
        f.setposition(self.x0, self.y0)
        f.pendown()
        f.pencolor(self.color)
        f.fillcolor(self.fill)
        for i in range(4):
            f.forward(self.size)
            f.right(90)
        f.end_fill()

class FigureTriangle(Figures):

    def __init__(self, x=0, y=0, side=10, color="black", fill_color="red"):
        super().__init__()
        self.color = color
        self.x0 = x
        self.y0 = y
        self.size = side
        self.fill = fill_color

    def draw(self):
        f = super().draw()
        f.setposition(self.x0, self.y0)
        f.pendown()
        f.pencolor(self.color)
        f.fillcolor(self.fill)
        for i in range(3):
            f.forward(self.size)
            f.right(120)
        f.end_fill()


window = turtle.Screen()
window.setup(500, 500)

c1 = FigureCircle(-140, -40, 40, "red", "blue")
c1.color = "green"
print(c1.size)
c1.size = 100
c1.draw()

s1 = FigureSquare()
s1.draw()

s2 = FigureSquare(130, 10, 60, "lime", "yellow")
s2.draw()

t1 = FigureTriangle(-200, 150, 80, "purple", "orange")
t1.draw()

turtle.done()