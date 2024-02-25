### Общий формат цикла с параметром
"""
for параметр in интервал (от начального значения до конечного значения, шаг изменения параметра цикла):
    тело цикла выполняется, если параметр цикла не достиг еще своего конечного значения.
    ............
    ............ continue - перепрыгнет итерацию, не завершив тело цикла
    ------------ break - остановит цикл 
    ************
else: # необязательный маркер цикла for будет выполнен только в том случае,
        если цикл не был «остановлен» оператором break.
        Таким образом, он будет выполнен только после того, как все элементы последовательности будут пройдены.
""" #
import random

# Командами break и continue мы можем прервать выполнение цикла или продолжить соответственно.
# Например, если решение задачи уже найдено и не требуется продолжать перебирать все элементы параметра цикла,
# то его можно прервать командой break. А командой continue, наоборот, можно пропустить итерацию.
# Обычно эти команды используют для скорости нахождения решений вместе с условием.

# Итерация по числам с нуля до 10 не включительно с шагом 2.
for i in range(0, 10, 2):
    print(i, end=" ")
print()
# Итерация по числам с 3 до 6 не включительно. Если шаг цикла не указан, то он равен 1.
for i in range(3, 6):
    print(i, end=" ")
print()

# итерация по числам с 6 до 3 не включительно с шагом -1
for i in range(6, 3, -1):
    print(i, end=" ")

for i in range(5):
    print("Привет!")

for _ in range(5):
    print("Привет!")



for _ in range(5):
    random.seed()
    a = random.randint(0,10)
    b = random.randint(0, 10)
    print(a,"и",b)
    if a == 0 and b == 0:
        continue
    if a == b:
        print(f"Вот они два одинаковых числа: {a}={b}")
        break
else:
    print("Одинаковых чисел не было!")


random.seed()
answer = 0 # инициализация суммы (обнуление)
for value  in range(100,201,5): # интервал и шаг изменения параметра цикла
    answer = answer + value # нахождение суммы чисел (тело цикла)
print(answer) # вывод ответа после завершения цикла

