# Кортеж (tuple) в Python является неизменяемым и упорядоченным набором объектов.
# Элементы кортежа могут быть любых типов данных, включая числа, строки, списки, другие кортежи и т.д.

# Пустой кортеж, кортеж из одного элемента
empty_tuple = ()
tuple1 = (42,)
print(tuple1)

# Кортеж из 2-х элементов
tuple2 = (3, 5)

# Кортеж из разнотипных элементов
student_info = ("Alex", 22, "C++")
print(student_info)


# Обращение к элементам кортежа по их индексу
x = tuple2[0]
y = tuple2[1]
print(x, y)

name = student_info[0]
age = student_info[1]
print("name:", name)
print("age:", age)

# student_info[1] = 23
# Обратимся к таблице: У Кортежа элементы неизменяемые, можно его переопределить
student_info = ("Alex", 23, "C++")
print(student_info)

student_info = student_info + (170,)
print(student_info)

# Обращение через элемент кортежа
for el in student_info:
    print(el)
print()

# Обращение через индекс кортежа
for i in range(len(student_info)):
    print(student_info[i])

# Изменение элементов кортежа невозможно
# del student_info[3]
student_info = ("Alex", 23, "C++")
list_student = list(student_info)
del list_student[2]
student_info =tuple(list_student)
print(student_info)
# indexes = student_info.index("С++")
# print(indexes)
# Кортеж содержит неизменяемые элементы! Поэтому не поддаётся сортировке самостоятельно


tuple1 = (12, 14, 50, 60, 80, 20, 90, 70, 15)
print(tuple1)
print(len(tuple1))
print(max(tuple1))
print(min(tuple1))
print(sum(tuple1))





