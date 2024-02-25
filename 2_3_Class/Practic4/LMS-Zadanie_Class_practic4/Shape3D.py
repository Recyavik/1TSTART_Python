# Практика 4.
# Создайте класс трехмерной фигуры Shape3D и три дочерних класса трехмерных фигур,
# например цилиндра, конуса и сферы. Используйте ссылку для изучения теоретических основ нахождения объема
# и площади этих фигур: https://egemaximum.ru/wp-content/uploads/2013/05/90.jpg
#
# Обеспечьте в программном коде возможность нахождения площади поверхности фигур и
# объема трёхмерной фигуры используя парадигму полиморфизма
# ООП (Полиморфизм позволяет обрабатывать объекты разных классов, но с одинаковыми методами, как однотипные).

import math

class Shape3D:

    def area(self):
        pass
    def volume(self):
        pass


class Sphere(Shape3D):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 4 * math.pi * (self.radius ** 2)

    def volume(self):
        return (4 / 3) * math.pi  * (self.radius ** 3)


class Cone(Shape3D):
    def __init__(self, radius, height, length):
        self.radius = radius
        self.height = height
        self.length = length

    def area(self):
        side_area = math.pi * self.radius * self.length
        total_area = math.pi * (self.radius ** 2)
        return total_area

    def volume(self):
        return (1 / 3) * math.pi  * (self.radius ** 2) * self.height


class Cylinder(Shape3D):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def area(self):
        side_area = 2 * math.pi * self.radius * self.height
        total_area = side_area + 2 * math.pi * (self.radius ** 2)
        return total_area

    def volume(self):
        return math.pi * (self.radius ** 2) * self.height


# Мы можем создать функцию, которая принимает список объектов
# типа «3D Фигура» и выводит на экран их площадь поверхности и объем фигуры:
def describe_3Dshapes(shapes):
    for shape in shapes:
        print(shape.__class__)
        print("Площадь поверхности:", shape.area())
        print("Объем фигуры:", shape.volume())
        print("_______________________")


sph = Sphere(20)
cyl = Cylinder(10, 10)
con = Cone(3, 4, 5)

describe_3Dshapes([sph, cyl, con])