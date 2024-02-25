import math
import random
import string


def print_ladder(message):
    for i in range(len(message)):
        print(message[:i])
    print(message)


print_ladder('Функции')
print()
print_ladder('Python')
print()
print_ladder('Функцию пишут для многократного обращения к ней')
print()


def area_rectangle(a, b):
    return a * b

s = area_rectangle(5, 6)
print('Площадь прямоугольника = ', s)
s = area_rectangle(5, 6)
print('Площадь прямоугольника = ', s)

def perimetr_rectangle(a, b):
    p = (a + b) * 2
    return p

p = perimetr_rectangle(b=5, a=6)
print('Периметр прямоугольника = ', p)
# def perimetr_rectangle(a, b):
#     global p1
#     p1 = (a + b) * 2
#     return p1
# print(p1)

def perimetr_area_circle(r):
    d = math.pi * 2 * r
    s = math.pi * r **2
    return d, s

d, s = perimetr_area_circle(100)
print('Длина окружности=', d)
print('Площадь окружности', s)

def report_school(ball, norma):
    percent = ball / norma
    if percent <= 0.5:
        assessment = 2
    else:
        assessment = round(5 * percent)
    return round(percent*100), assessment

p, a = report_school(5, 5)
print(f'Качество = {p}% Оценка: {a}')
p, a = report_school(6, 10)
print(f'Качество = {p}% Оценка: {a}')
p, a = report_school(18, 21)
print(f'Качество = {p}% Оценка: {a}')


def get_password(size):
    password = ''
    alphabet = list(string.ascii_letters + string.digits + string.punctuation)
    # print(alphabet)
    for _ in range(size):
        symbol = random.choice(alphabet)
        password += symbol
    return password

print(get_password(8))

# Конструкцию **kwargs нельзя располагать до *args. Если это сделать — будет выдано сообщение об ошибке.