# Matplotlib предлагает множество возможностей для настройки внешнего вида графика,
# включая цвета, шрифты и типы линий.
# Вот примеры использования некоторых методов и свойств для настройки этих аспектов:


import matplotlib.pyplot as plt
import numpy as np

# Создаем фигуру
fig = plt.figure(figsize=(8, 6))  # Задаем размер фигуры (ширина, высота) в дюймах
# Создаем оси внутри фигуры
ax = fig.add_subplot(1, 1, 1)  # Создаем одни оси (1 строка, 1 столбец, индекс 1)
# Добавляем данные и настраиваем график
x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
cos, sin = np.cos(x), np.sin(x)
# plt.plot(x, cos)
# plt.plot(x, sin)
plt.plot(x, cos, color='blue', label="y=cos(x)")
plt.plot(x, sin, color='red', label="y=sin(x)")

# Добавляем подписи осей и заголовок
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_xlabel('X-axis', fontname='Arial', fontsize=12)
ax.set_ylabel('Y-axis', fontname='Arial', fontsize=12)

ax.set_title('Графики функции')
# Добавляем сетку
ax.grid(True)
# Добавим цвета
fig.patch.set_facecolor('lightgray')
ax.set_facecolor('white')
# Отображаем график
plt.legend(['Cos(x)', 'Sin(x)'], loc='upper left', frameon=True, fontsize=10, title='Легенда')

plt.show()
