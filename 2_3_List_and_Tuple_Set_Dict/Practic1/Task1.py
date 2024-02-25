# В Python список (list) является одним из встроенных типов данных
# и представляет собой изменяемую # последовательность значений,
# которые могут быть различных типов, включая числа, строки, другие списки и т.д.

""" 
Рисунок list_1
""" #
list1 = ['a', 'b', 'c']
print(list1[0])

list2 = [11, 22, 33, 44, 55]
print(list1[0])



list_empty = [] # Через литерал
list1 = list() # Через функцию
list2 = [11, 12, 13, 14, 15]
list3 = ["Python", "C#", "Java Script"]
# На начало 2023 года общее население России почти 150_000_000, а плотность 8.55 человека на кв.км.
list4 = ["Россия", 150_000_000, 8.55]

""" 
Рисунок list_2_index
""" #

# Обращение к элементу списка по индексу
print(list3[1])
print(list3[2])
# Обращение ко всему списку по имени
print(list4)
print(list2)
print(list2[0])
print(list2)

# Добавление элементов списка
""" 
Рисунок list_3_append
""" #
list0 = [99, 66]

list0.append(77)
list0.append(88)
print(list0)

# Вставка элементов списка
""" 
Рисунок list_4_insert
""" #
list0.insert(2, 5)
list0.insert(2, 1)
print(list0)

# Замена элементов списка
""" 
Рисунок list_5_edit
""" #
new_list = list0
new_list[0] = 101
print(new_list)


# Удаление элемента из списка по значению
""" 
Рисунок list_6_del
""" #

list1 = [11, 22, 33, 44, 55, 66, 77, 88]
list1.remove(77)
print(list1)
# Удаление элемента из списка по индексу
del list1[2]
del list1[:3]
print(list1)
# Управляемое удаление
list1 = [1, 2, 3, 4, 5, 6, 7, 8]
list1.pop() #
print(list1)
list1.pop() # Неконтролируемое удаление последнего элемента
print(list1)
list1.pop(0)    # Удаление по индексу
print(list1)
list1.pop(list1.index(3)) # удаление по значению
print(list1)

# Поиск элемента в списке
""" 
Рисунок list_7_in
""" #
colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
logic = "lime" in colors
print(logic)

print(colors.index("green"))
print(colors.index("pink"))


""" 
Рисунок list_8_extend
""" #
# Соединение списков
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
new_list = list1 + list2
print(new_list)
new_list.extend([11, 22, 33])
print(new_list)


""" 
Рисунок list_9_copy
""" #
# Копирование списка
a = [1, 2, 3]
b = a  # переменной b присваивается не значение списка a, а его адрес
print(id(a), id(b))
# a и b ссылаются на один и тот же список
b.append(4)
print(a, b)
# [1, 2, 3, 4] [1, 2, 3, 4]

a = ["кот", "слон", "змея"]
b = a.copy()
print(id(a), id(b), a, b)
# 56467336 56467016 ['кот', 'слон', 'змея'] ['кот', 'слон', 'змея']

d = list(a)
print(id(a), id(d), a, d)
# 56467336 60493768 ['кот', 'слон', 'змея'] ['кот', 'слон', 'змея']

import copy
e = copy.copy(a)  #
print(id(a), id(e), a, e)
# 56467336 60491304 ['кот', 'слон', 'змея'] ['кот', 'слон', 'змея']

f = copy.deepcopy(a)
print(id(a), id(f), a, f)
# 56467336 56467400 ['кот', 'слон', 'змея'] ['кот', 'слон', 'змея']

c = a[:]  # устаревший синтаксис
print(id(a), id(c), a, c)
# 56467336 60458408 ['кот', 'слон', 'змея'] ['кот', 'слон', 'змея']

a = ["кот", "слон", "змея"]

b = a[2:]  # с 2-го элемента (включительно) до конца списка
print(b)
# ['змея']

c = a[:2]  #  с начала списка по 2-й элемент
print(c)
# ['кот', 'слон']

d = a[1:2]  #  с 1-го элемента (включительно) по 2-й элемент
print(d)
# ['слон']

a = [1, 2, 3, 4, 5, 6, 7, 8]
e = a[0:8:2]  # c 0-го элемента по 8-й элемент с шагом 2
print(e)
# [1, 3, 5, 7]



# Перебор элементов списка по индексу
""" 
Рисунок list_A_for
""" #
for i in range(0, len(list3)):
    print(list3[i])

# Порядковый перебор элементов списка
for el in list3:
    print(el)

list6 =[1, 2, 3, 4, 5]
# Замена всех элементов списка
for i in range(0, len(list6)):
    list6[i] = list6[i] * 3
    print(list6[i], end=' ')
print()

# Замена чётных значений элементов списка
for i in range(0, len(list6)):
    if list6[i] % 2 == 0:
        list6[i] = int(list6[i] / 2)
    print(list6[i], end=' ')
print()

# Замена элементов списка с чётными номерами
for i in range(0, len(list6)):
    if i % 2 == 0:
        list6[i] = int(list6[i] * 5)
    print(list6[i], end=' ')
print()


#Элемент списка сам может быть списком
list1.append([33, 44, 99])
print(list1)

# Сортировка списка
list2 = [31, 12, 43, 14, 25, 99, 8, 15]
print(list2)
list2.sort()
print(list2)
list2.reverse()
print(list2)

# min, max, sum
print(min(list2))
print(max(list2))
print(sum(list2))



#Связывание двух списков
colors = ['red', 'green', 'blue']
codes = [0xff0000, 0x00ff00, 0x0000ff]
for color, code in zip(colors, codes):
    print(color, hex(code))

"""

list.append(x)  — позволяет добавлять элемент в конец списка;
list1.extend(list2)  — предназначен для сложения списков;
list.insert(i, x)  — служит для добавления элемента на указанную позицию (i  — позиция,  x — элемент);
list.remove(x)  — удаляет элемент из списка (только первое вхождение);
list.clear() — предназначен для удаления всех элементов (после этой операции список становится пустым []);
list.copy() — служит для копирования списков.
list.count(x) — посчитает количество элементов x  в списке;
list.index(x) — вернет позицию первого найденного элемента x в списке;
list.pop(i) — удалит элемент из позиции i;
list.reverse() — меняет порядок элементов в списке на противоположный;
list.sort() — сортирует список.

""" #
# Генератором списка называется способ построения списка
# с применением выражения к каждому элементу, входящему в последовательность.
# Есть схожесть генератора списка и цикла for.

c = [c * 3 for c in 'Python']
print(c)

nums = [i for i in range(1, 15)]
print(nums)

elements = [c for c in range(0, 10, 2)]  # от 0 (включительно) до 10 с шагом 2
print(elements)

# Генерация списка
list2 = [11, 12, 13, 14, 15]
list5 = [el*2 for el in list2]
print(list5)

# Генерация списка с фильтром
list2 = [11, 12, 13, 14, 15]
list5 = [el*2 for el in list2 if el %2 ==0]
print(list5)