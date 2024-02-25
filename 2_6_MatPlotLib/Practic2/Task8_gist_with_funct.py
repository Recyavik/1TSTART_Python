# pip install matplotlib
# pip install numpy

import matplotlib.pyplot as plt
import numpy as np

# 9 Ширина
width = 0.4

x = list(range(0, 7))
y1 = [2, 5, 2, 7, 11, 1, 7]
y2 = [3, 4, 1, 6, 9, 2, 6]
y3 = [el**2 for el in x]
y4 = [el*3  for el in x]
# 12 Разделение областей
plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)

# 9 Ширина
x_indexes = np.arange(len(x))
# 11 переопределение
plt.xticks(x_indexes, ['ПН', 'ВТ', 'СР', "ЧТ", "ПТ", "СБ", "ВС"])

# 2 Добавление заголовка
plt.title("Линейный график", fontsize=16, fontweight="bold", color="blue")
# 3 Подпись осей
plt.xlabel("Значения x", fontsize=16, color="green")
plt.ylabel("Значения y", fontsize=16, color="green")
# 4 Сетка
plt.grid()
# 5 Подпись графика
plt.plot(x, y3, '--', label="f(x)=x^2", linewidth=3, color="red", marker='o')
# Ключевые точки
plt.plot(x, y4, '', label="f(x)=3x", linewidth=2, color="Indigo", marker='s') # > ^
# 7 Цвет
ax = plt.gca()
ax.set_facecolor("Aquamarine")
# 8 Столбики
plt.legend()


# 12
plt.subplot(1,2,2)
plt.title("Гистограмма", fontsize=16, fontweight="bold", color="green")
plt.xticks(x_indexes, ['ПН', 'ВТ', 'СР', "ЧТ", "ПТ", "СБ", "ВС"])

plt.xlabel("Дни недели", fontsize=16, color="green")
plt.ylabel("Новые значения y", fontsize=16, color="green")

# 9 Ширина
plt.bar(x_indexes - (width/2), y1, label='Телевизоры 55" ', width=width, color="MediumVioletRed")
plt.bar(x_indexes + (width/2), y2, label='Телевизоры 55" ', width=width, color="LightSeaGreen")
# 6 Легенда
plt.legend()
plt.annotate('Растущий тренд', xy=(4, 8), xytext=(4, 5),
            arrowprops=dict(facecolor='blue', arrowstyle='->'),
            fontsize=8, color='black')

# Сохраняем график в формате PNG
# Matplotlib предоставляет возможность сохранять созданные графики в различные форматы файлов,
# включая PNG, PDF и SVG. Вот примеры сохранения графиков в эти форматы:

plt.savefig('grafik.png', dpi=300)  # указываем имя файла и разрешение (dpi)
plt.savefig('grafik.pdf')
plt.savefig('grafik.svg')


plt.show()