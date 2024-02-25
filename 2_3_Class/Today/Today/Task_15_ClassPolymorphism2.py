# Полиморфизм (Polymorphism). Полиморфизм позволяет обрабатывать объекты разных классов,
# но с одинаковыми методами, как однотипные. Таким образом, код становится более гибким и расширяемым.

class Shape:

    def __init__(self, name="Фигура"):
        self.__name = name

    def __str__(self):
        return self.__name

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Окружность")
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Прямоугольник")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Triangle(Shape):
    def __init__(self, a, b, f):
        super().__init__("Треугольник")
        self.a = a
        self.b = b
        self.f = f

    def area(self):
        p = (self.a + self.b + self.f) / 2
        return (p * ((p-self.a) * (p-self.b) * (p-self.f))) ** 0.5

    def perimeter(self):
        return self.a + self.b + self.f


# Мы можем создать функцию, которая принимает список объектов
# типа «Фигура» и выводит на экран их площадь и периметр:
def describe_shapes(shapes):
    for shape in shapes:
        print(shape)
        print("Area:", shape.area())
        print("Perimeter:", shape.perimeter())


c = Circle(20)
r = Rectangle(10, 10)
t = Triangle(3, 4, 5)
t.name = "Квадрат"
describe_shapes([c, r, t])

# Наследование

# Полиморфизм (Polymorphism). Полиморфизм позволяет обрабатывать объекты разных классов,
# но с одинаковыми методами, как однотипные.
#
# Таким образом, код становится более гибким и расширяемым.