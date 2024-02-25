
# a * x**2 + b * x + c = 0

a, b, c = map(int, input("Введите коэффициенты через пробел:").split())
d = b ** 2 - 4 * a * c
if d < 0:
    print("Нет корней!")
elif d == 0:
    x1 = x2 = ((-b + d ** 0.5)) / (2 * a)
    print("\x1b[93m" + "x1= " + "\x1b[0m", x1)
    print("\x1b[92m" + "x2= " + "\x1b[0m", x2)

else:
    x1 = ((-b + d ** 0.5)) / (2 * a)
    x2 = ((-b - d ** 0.5)) / (2 * a)
    print("\x1b[93m" + "x1= " + "\x1b[0m", x1)
    print("\x1b[92m" + "x2= " + "\x1b[0m", x2)

