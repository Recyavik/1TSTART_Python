# Matplotlib предоставляет пакет pyplot, который используется для построения графика заданных данных.
# Matplotlib.pyplot – это набор функций командного стиля, которые заставляют matplotlib работать как MATLAB.
# Пакет pyplot содержит множество функций, которые используются для создания фигуры, создания ее области построения,
# дополнения графика метками, проведения некоторых линий в области построения и т. д.

import matplotlib.pyplot as plt
import numpy as np

# 9 Ширина
width = 0.4

# Визуализировать продажи телевизоров 50 и 55 дюймов
x = list(range(0, 7))
y1 = [2, 5, 2, 7, 11, 1, 7]
y2 = [3, 4, 1, 6, 9, 2, 6]
y3 = [el**2 for el in x]
y4 = [el * 3 for el in x]
# 9 Ширина
x_indexes = np.arange(len(x))
# 11 переопределение
plt.xticks(x_indexes, ["ПН", "ВТ", "СР", "ЧТ", "ПТ", "СБ", "ВС"])

# 2 Добавление заголовка
plt.title("Линейный график", fontsize=16, fontweight="bold", color="blue")
# 3 Подпись осей
plt.xlabel("Значения x", fontsize=16, color="green")
plt.ylabel("Значения y", fontsize=16, color="green")
# 4 Сетка
plt.grid()
# 5 Подпись графика
plt.plot(x, y3, "--", label="f(x)=x^2", linewidth=3, color="red", marker="o")
# Ключевые точки
plt.plot(x, y4, "", label="f(x)=3x", linewidth=2, color="Indigo", marker="s")  # > ^
# 7 Цвет
ax = plt.gca()
ax.set_facecolor("Aquamarine")
# 8 Столбики
plt.bar(x, y1, label='Телевизоры 55" ')
plt.bar(x, y2, label='Телевизоры 50" ')
# 9 Ширина
# plt.bar(x_indexes - (width/2), y1, label='Телевизоры 55" ', width=width)
# plt.bar(x_indexes + (width/2), y2, label='Телевизоры 55" ', width=width)

# 6 Легенда
plt.legend()
plt.show()
