# Программа нахождения корней квадратного уравнения
import math


a, b, c = map(int, input("Введите через пробел коэффициенты квадратного уравнения:").split())
d = b ** 2 - 4 * a * c
if d < 0:
    print("Нет корней, так как дискриминант меньше нуля:", d)
elif d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print("x1 = %4.2f" % x1)
    print("x2 = %4.2f" % x2)
else:
    x2 = x1 = (-b + math.sqrt(d)) / (2 * a)
    print("x1 = x2 = {x1:4.2f}".format(x1=x1))
