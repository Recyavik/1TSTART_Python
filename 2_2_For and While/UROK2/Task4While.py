# ЦИКЛ while (алгоритмическая структура повтора последовательности с предусловием)
""" 
параметр цикла = начальное значение

while условие_с_параметром:
    тело цикла, выполняется если условие истинно
    ............
    ............ continue - перепрыгнет итерацию, не завершив тело цикла
    ------------ break - остановит цикл 
    ************
    параметр = параметр + шаг

""" #
password = 1245
user_pincode = 0
while True:
    user_pincode = int(input("Введите пин-код:"))
    if user_pincode == password:
        print("\x1b[92m Доступ разрешён! \x1b[0m")
        break
    else:
        print("\x1b[91m Пин-код не верный.\x1b[0m Доступ запрещен!")

print("Добро пожаловать!")



x = 2
while x <= 15:
    print(x, end=' ')
    x = x + 1
print()

x = 3
while x <= 30:
    if x % 10 == 7 or x % 10 == 8:
        x = x + 1
        continue
    print(x, end=' ')
    x = x + 1
print()


minutes = 0  # начальное значение
while minutes <= 59:  # пока условие == истина выполнять тело цикла
    print(minutes, end=" ")  # тело цикла
    minutes = minutes + 1  # изменение параметра цикла с шагом + 1
print()

### Пример цикла с предусловием в обратную сторону (таймер)
minutes = 59  # начальное значение
while minutes >= 0:  # пока условие == истина выполнять тело цикла
    print(minutes, end=" ")  # тело цикла
    minutes = minutes - 1  # изменение параметра цикла с шагом -1
print()

# Вывести на экран сумму всех чисел кратных 5 от 100 до 200, т.е. 100 + 105 + 110 + 115 +... + 195 + 200
answer = 0  # инициализация суммы (обнуление)
value = 100  # начальное значение
while value <= 200:  # пока условие == истина выполнять тело цикла
    answer = answer + value  # нахождение суммы чисел (тело цикла)
    value += 5  # изменение параметра цикла с шагом + 5 (входит в тело цикла)
print(answer)  # вывод ответа после завершения цикла

### Пример цикла с предусловием "Степень двойки в обратном порядке"
# Вывести на консольный экран результат степеней двойки от 7 до 0,
degree = 7
while degree >= 0:
    print(f"2 в степени {degree} = {2**degree}")
    degree -= 1

### Пример вывода на экран эмулятора прогресс индикатора в процентах  0%, 1%, 2%, ....,99%, 100%
import time
import sys

i = 0
while i <= 100:
    i += 1
    print("\b\b\b\b\b\b\b", end="")
    print("{0:3}%".format(i), end="")
    sys.stdout.flush()
    time.sleep(0.1)

# Цикл может быть внутри другого цикла. Тогда при каждой итерации внешнего цикла внутренний цикл начинается сначала.
### Пример цикла с предусловием для вывода значений часов с отображением минут и секунд
minutes = 0  # начальное значение минут
while minutes <= 59:  # пока условие истина выполнять тело 1-го цикла
    seconds = 0  # начальное значение секунд сбрасывается каждый раз, поэтому стоит внутри 1-го цикла
    while seconds <= 59:  # пока условие истина выполнять тело 2-го цикла
        print(minutes, ":", seconds)  # вывод на экран
        seconds += 1  # изменение параметра цикла секунд с шагом + 1
    minutes += 1  # изменение параметра цикла минут с шагом + 1 только после всех проходов 2-го цикла

### Полная версия программы часов будет выглядеть так:
import time

minutes = 0  # начальное значение минут
while minutes <= 59:  # пока условие истина выполнять тело 1-го цикла
    seconds = 0  # начальное значение секунд сбрасывается каждый раз, поэтому стоит внутри 1-го цикла
    minutes_str = str(minutes)
    if minutes < 10:
        minutes_str = "0" + minutes_str
    while seconds <= 59:  # пока условие истина выполнять тело 2-го цикла
        print("\b\b\b\b\b", end="")
        seconds_str = str(seconds)

        if seconds < 10:
            seconds_str = "0" + str(seconds)
        print(f"{minutes_str}:{seconds_str}", end="")
        seconds += 1  # изменение параметра цикла с шагом + 1
        time.sleep(1.0)  # пауза между выводом.
    minutes += 1  # изменение параметра цикла минут с шагом + 1 только после всех проходов 2-го цикла
