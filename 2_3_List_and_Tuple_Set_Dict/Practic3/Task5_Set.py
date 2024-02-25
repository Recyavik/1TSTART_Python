#  Множество — обозначает набор или совокупность неких уникальных элементов,
#  которые обладают каким-то общим свойством
#  и сгруппированных под одним именем.
#  Соответствующая структура данных в языке Python называется set.
s1 = {}
s2 = {1, "python.ru", 20.67}
print(s2, type(s2))
# Нет ограничений на количество элементов в объекте set,
# но запрещено добавлять элементы изменяемых типов, такие как список или словарь.
# s3 = {[1, 2, 3, 4, 5]}
s3 = set([11, 12, 13, 14, 15])
print(s3, type(s3))
s4 = {"Python"}
print(s4, type(s4))
s5 = set("Python")
print(s5, type(s5))
s4 = {}
s3 = set()  # Это создаст пустое множество


# s5 = {1, "python.ru", 20.67, [1,2,3] }

# Добавление одного элемента
set22 = {}
# set22.add()

set1 = {1, 3, 4}
k = 6
set1.add(2)
set1.add(9)
set1.add(k)
set1.add(3)
print(set1)



# Добавление списка элементов
set2 = {1, 2, 3}
set2.update([4, 5, 6])
print(set2)  #  {1, 2, 3, 4, 5, 6}

list1 = [4, 3, 6, 9, 5, 5, 4, 4, 4, 5, 5]
set3 =set(list1)
print(set3)

# Удаление
# remove()
# discard()
# pop()

set1 = {1, 2, 3, 4, 'a', 'p'}
set1.remove(2)
print(set1)
# set1.remove(5) # Выдаст ошибку

# Удалить, без ошибки
set1 = {1, 3, 4, 'a', 'p'}
set1.discard('a')
print(set1)
set1.discard(6)
print(set1)

# Неконтролируемое удаление
set1 = {1, 3, 4, 'p'}
set1.pop()

# Функции принадлежности
print(4 in set1)
print(8 in set1)

# Другие функции
new_s1 = s1.copy() #Копирование
s1.clear() # Очистка
print(new_s1)
# del new_s1  - Удаляет целиком
# print(new_s1)

set3 = {88, 22, 99, 44, 55, 66, 77, 11, 33}
print(set3)
print(max(set3))
print(min(set3))
print(sum(set3))
print(len(set3))




# Объединение множеств
A = {1, 2, 3}
B = {2, 3, 4, 5}
C = A | B  # используя символьный метод
C = A.union(B) # используя метод union
print(C)

# Пересечение множеств
A = {1, 2, 3, 4}
B = {3,4,5,6}
C = A & B  # используя символьный метод
C = A.intersection(B)  # используя метод intersection

# Разность
A = {1, 2, 3, 4}
B = {3,4,5,6}
C = A - B # используя символьный метод
C = A.difference(B) # используя метод difference
print(C)

#  Bonus Как сделать уникальным список
list1 = ["red", "green", "green", "blue"]
list1 = list(set(list1))
print(list1)

A = {1, 2, 3, 4}
A.add(5)
print(A)
B = frozenset({3,4,5,6})
# B.add(5)

