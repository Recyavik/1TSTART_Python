# При создании графиков с использованием библиотеки Matplotlib, основными компонентами,
# с которыми нужно работать, являются фигура (Figure), оси (Axes) и подписи (Labels).
# Вот примеры работы с этими компонентами:
# Фигура (Figure).
# Фигура представляет собой контейнер, который содержит все элементы графика.
# Вы можете настроить размер фигуры и другие свойства с помощью методов объекта Figure.
import matplotlib.pyplot as plt
import numpy as np

# Создаем фигуру
fig = plt.figure(figsize=(8, 6))  # Задаем размер фигуры (ширина, высота) в дюймах
# Создаем оси внутри фигуры
ax = fig.add_subplot(1, 1, 1)  # Создаем одни оси (1 строка, 1 столбец, индекс 1)
# Добавляем данные и настраиваем график
x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
cos, sin = np.cos(x), np.sin(x)
plt.plot(x, cos, color='blue', label="y=cos(x)")
plt.plot(x, sin, color='red', label="y=sin(x)")
plt.legend(loc='upper left', frameon=False)

# Добавляем подписи осей и заголовок
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Графики функции')
# Отображаем график
plt.show()
