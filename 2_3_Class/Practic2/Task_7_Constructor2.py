class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b
# Магический метод __str__() в Python используется для определения строкового представления объекта.
# Метод __str__() вызывается функциями str(), format() и print(), когда они применяются к объекту.

    def __str__(self):
        return f'Rectangle {self.a}x{self.b} = '


class Square:
    def __init__(self, a):
        self.a = a

    def get_area(self):
        return self.a ** 2

    def __str__(self):
        return f"Square {self.a} ="
# Метод __str__() используется не только функцией print(), но и другими встроенными функциями и методами,
# такими как str(), format(). Это значит, что если вы переопределите __str__(), вы сможете контролировать,
# как объекты вашего класса будут отображаться в различных контекстах.


class Circle:
    def __init__(self, r):
        self.r = r

    def get_area(self):
        return 3.14*self.r ** 2

    def __str__(self):
        return f"Circle radius {self.r} ="


rect1 = Rectangle(5, 7)
rect2 = Rectangle(12, 3)

sq1 = Square(5)
sq2 = Square(7)

cr1 = Circle(3)
cr2 = Circle(2)

figures = [rect1, rect2, sq1, sq2, cr1, cr2]
for figure in figures:
    print(figure, figure.get_area())

# Магический метод __str__() — это инструмент, который позволяет вам контролировать,
# как объекты ваших классов преобразуются в строки. Переопределяя __str__(),
# вы можете сделать вывод ваших объектов более понятным и информативным,
# что может быть очень полезно при отладке и взаимодействии с пользователем.
