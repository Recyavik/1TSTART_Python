# Напишите функцию product (number), которая будет подсчитывать произведение цифр числа.
# Считывайте значение числа с помощью input. В функции используйте метод for, чтобы перебрать цифры числа.
# При переборе цифр числа, не забудьте их привести к типу int. Напечатайте результат в конце выполнения программы.

def product(number):
    p = 1
    while number // 10 > 0:
        p *= (number % 10)
        number = number // 10
    return p

n = product(123)
print(n)

def product(number):
    p = 1
    for i in range(len(str(number))):
        p *= int(str(number)[i])
    return p

n = product(123)
print(n)
