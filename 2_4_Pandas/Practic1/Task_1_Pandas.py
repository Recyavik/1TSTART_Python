# https://pypi.org/

# Pandas – это мощная библиотека для анализа данных, построена поверх языка программирования Python.
# Она предоставляет высокоуровневые структуры данных и инструменты для эффективной
# обработки и анализа данных. Pandas является одной из наиболее популярных библиотек для работы
# с данными в Python, и широко используется в индустрии и научном сообществе.
# Pandas предоставляет две основные структуры данных: Series и DataFrame.
# Series – это одномерная индексированная структура данных, которая может содержать различные
# типы данных, включая числа, строки и объекты Python.
# DataFrame – это двумерная структура данных, # представляющая таблицу с рядами и столбцами.
# DataFrame может быть рассмотрен как аналог таблицы в реляционной базе данных или электронной таблицы Excel.
# Основная цель Pandas – упростить работу с данными. Она предлагает множество функций и методов для чтения,
# записи, фильтрации, агрегирования, группирования и визуализации данных.
# Благодаря своим мощным функциональным возможностям, Pandas позволяет быстро и эффективно
# манипулировать большими объемами данных.
# Давайте рассмотрим несколько ключевых возможностей Pandas:

# pip install pandas
# pip install np
import pandas as pd  # type: ignore
import numpy as np

# В Pandas, структура данных Series представляет собой одномерный массив с метками (индексами)
# для каждого элемента.
# Она может содержать данные различных типов, включая числа, строки, булевы значения и объекты Python.
# Создание Series из списка чисел
numbers = [1, 2, 3, 4, 5]
series = pd.Series(numbers)
print(series)

numbers = [1, 2, 13, 4, 5.0, 2]
series = pd.Series(numbers)
print(series)
vals = series.values  # возвращает массив значений в Series.
print(vals)
indexes = series.index  # возвращает индексы в Series.
print(indexes)
tail_n = series.tail(3)  # возвращает последние n элементов в Series.
print(tail_n)
head_n = series.head(2)  # возвращает первые n элементов в Series.
print(head_n)
# вычисляет основные статистические показатели о Series (среднее, стандартное отклонение, минимум, максимум)
des = series.describe()
print(des)
uniq = series.unique()
print(uniq)
count = series.count()
print(count)
val_count = series.value_counts()
print(val_count)


# В качестве data могут выступать: массив numpy, словарь, число.
s = pd.Series(np.linspace(0, 1, 5))
print(s)

d = {"a": 11, "b": 12, "c": 13, "g": 14}
print(pd.Series(d))
print()
print(pd.Series(d, index=["a", "b", "c", "d"]))

s = pd.Series(np.arange(5), index=["a", "b", "c", "d", "e"])
print("Выбор одного элемента")
print(s["a"])
print("Выбор нескольких элементов")
print(s[["a", "d"]])
print("Срез")
print(s[1:])
print("Поэлементное сложение")
print(s + s)

# Объекты Series имеют атрибут name со значением имени набора данных,
# а также атрибут index.name с именем для индексов:
s = pd.Series(np.arange(5), index=["a", "b", "c", "d", "e"])
s.name = "Данные"
s.index.name = "Индекс"
print(s)


import pandas as pd

data = [10, 20, 30, 40, 50]
index = ["a", "b", "c", "d", "e"]
# В аргумент index передаётся список меток осей.
# Метка может быть числом, но чаще используются метки-строки.
series = pd.Series(data, index=index)
print(series)
print(series["b"])  # Доступ к элементу по индексу
print(series[2:3])  # Доступ к элементу по позиции
print(series[1:4])  # Индексация по диапазону
filtered_series = series[series > 30]
print(filtered_series)
new_series = series.drop("c")  # Удаление элемента по индексу
print(new_series)

series["a"] = 35  # Изменение значения элемента по индексу
series[1:4] = 0  # Изменение значения элементов по позиции
print(series)
