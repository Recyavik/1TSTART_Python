name = input("Как тебя зовут? ")
print("Привет, " + name + "!")
print("Привет {}!".format(name))

# Всё что вводит пользователь с помощью input - это строка
a = input("Введите первое число: ")
b = input("Введите второе число: ")
sum = a + b
print("Sum =", sum)

a = input("Введите первое число: ")
b = input("Введите второе число: ")
sum = int(a) + int(b)
print("Sum =", sum)

a, b = map(int, input("Введите два числа через пробел").split())
sum = a + b
print(sum)

# f - строка
print(f"{a}+{b}={sum}")

print("{}+{}={}".format(a, b, sum))

# Метод format
name = "Python"
print("Привет {}!".format(name))

print("{0}+{1}={2}".format(a, b, sum))

print("Задача №{r:4d} Ответ = {w:6.2f}".format(r=1134, w=112.5534))

print(
    "{0} {1} января празднует {other} день рождения".format(
        "Никита", "25", other="15-ый"
    )
)

text = "Этот текст хочу расположить в центре"
print(text.center(50, "*"))

print("%3d %4d" % (16, 77))

z = 5
k = "5"
try:
    print(f"Вычисление {z+1} прошло успешно")
    print(f"Вычисление {k+1} прошло успешно")
except Exception as err:
    print('Возникла ошибка: "{}"'.format(err))


print("\033[33m\033[44m {}".format(text))
