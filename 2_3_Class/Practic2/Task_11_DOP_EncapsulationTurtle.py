import turtle


class TurtlePen:
    def __init__(self, pen_color="black"):
        self.__pen = turtle.Turtle()
        self.__pen.color(pen_color)

    def draw_square(self, size):
        for i in range(4):
            self.__pen.forward(size)
            self.__pen.right(90)

    def draw_circle(self, radius):
        self.__pen.circle(radius)


pen = TurtlePen("blue")
pen.draw_square(100)
pen.draw_circle(50)
# pen.__pen.forward(50)
