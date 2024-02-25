# Напишите программу на Python, которая запрашивает
# у пользователя начальное и конечное значения диапазона целых чисел,
# а затем вычисляет сумму всех чисел в этом диапазоне.

a = input("Введите начальное значение диапазона: ")
b = input("Введите конечное значение диапазона: ")
try:
    first = int(a)
    second = int(b)
    if first > second:
        first, second = second, first
    answer = 0
    for p in range(first, second + 1):
        answer += p
    print(answer)
except ValueError:
    print("Ошибка! Введите числа через пробел")