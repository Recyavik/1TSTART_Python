# Различают три основных вида алгоритмов:

# Линейный алгоритм.
# Разветвляющийся алгоритм.
# Циклический алгоритм.

# В нашей жизни порядок играет важное значение. Правильно сложенный
# инструмент, школьные, продукты питания

# Типы данных в программировании появились с развитием языков программирования,
# чтобы улучшить обработку информации
# и управление данными. Они позволяют классифицировать информацию
# в соответствующие категории, такие как числа, строки,
# логические значения и так далее.
a = 5
a = 14
print(a)
print(type(a))
z = 150_000_000
print("Население России =", z)
print(z, type(z))
print(a, z)

d, c = 14, 15
print("d=", d, "c=", c)
k = m = f = 0
print(k, m, f)

p = 8.5
print("Плотность населения =", p, "чел/кв.км")
print(p, type(p))
# нельзя 1x?, резервные слова
name = "Python"
print(name, type(name))
first_name = "Alex"
print(first_name, type(first_name))
logic = True
flag = False
print(logic, type(logic))
print(flag, type(flag))

s = range(8, 16, 2)
print("Диапазон s = ", s, type(s))

# Коллекции
list_number = [15, 16, 14, 12]
print("Список", list_number, type(list_number))


# tuple(Кортеж) - неизменяемая последовательность значений. Значения могут быть разных типов
tuple_ages = (14, 15, 16, 15)
print("Кортеж", tuple_ages, type(tuple_ages))

# dict Словарь - это структура данных, содержащая пару ключ-значение для хранения ассоциативных данных
hockey_top_name = {"Ovechkin": 192, "Malkin": 191, "Kovalchuk": 191}
print("Словарь", hockey_top_name, type(hockey_top_name))

# set Множество уникальных значений
ages = {14, 15, 16, 15, 14, 10, 10, 10, 10, 15}
print("Множество:", ages, type(ages))

# Специальный объект внутри Python. Означает пустое значение и всегда считается ложью
e = None
print(e, type(e))


result1 = 8 + 12
result2 = "12" + "45"
print(result1, "-", type(result1))
print(result2, "-", type(result2))
new_string = str(8) + str(12)
print(new_string, "-", type(new_string))
new_value = int("12") + int("45")
print(new_value, "-", type(new_value))
# new_value2 = int("ох!") + int("ах!")
# print(new_value2, '-', type(new_value2))

value1, value2 = 7, 2
print(value1 + value2)
print(value1 - value2)
print(value1 * value2)
print(value1**value2)
print(value1 / value2)
print(value1 // value2)
print(value1 % value2)

world = "cherry"
print(world * 3)
d = len(world)

# f строка
a = 5
b = 6
print(f"{a}+{b}={a+b}")
c = a + b
print(f"{a}+{b}={c}")
