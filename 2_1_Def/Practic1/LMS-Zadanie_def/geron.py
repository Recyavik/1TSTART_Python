# Напишите функцию нахождения периметра и площади треугольника
# по формуле Герона и функцию определения существования треугольника:
# «Сумма любых двух сторон треугольника не может быть меньше третьей стороны»
# Формулы вычисления можно найти здесь:
# https://calculat.ru/wp-content/uploads/2018/11/ploshad-treugolnika-po-trem-storonam.png


def check_sum(a1, a2, a3):
    if a1 + a2 <= a3:
        return False
    else:
        return True

def check_triangle(a, b, c):
    if check_sum(a, b, c) == check_sum(b, c, a) == check_sum(a, c, b) == True:
        return True
    else:
        return False

def geron(a, b, c):
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return p, s

a, b, c = 20, 10, 15
if check_triangle(a, b, c):
    p, s = geron(a, b, c)
    print(f'Периметр треугольника со сторонами {a},{b},{c} = {p}')
    print(f'Площадь треугольника со сторонами {a},{b},{c} = {s}')
else:
    print(f'Треугольник со сторонами {a},{b},{c} не существует!')

a, b, c = 20, 10, 30
if check_triangle(a, b, c):
    p, s = geron(a, b, c)
    print('Периметр треугольника =', p)
    print('Площадь треугольника = ', s)
else:
    print(f'Треугольник со сторонами {a},{b},{c} не существует!')
