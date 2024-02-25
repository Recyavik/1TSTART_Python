# Постройте спираль Архимеда с помощью библиотеки Matplotlib по следующим формулам:
# значения угла alpha в радианах от 0 до 10 с шагом 0.2
# значения r = 0.5 * alpha
# значения х = r * cos(alpha)
# значения y = r * sin(alpha)


import matplotlib.pyplot as plt
import numpy as np
import math

# Создаем фигуру
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(1, 1, 1)
alpha = np.linspace(0, 10, 500, endpoint=True)
x , y = list(), list()
for a in alpha:
   r = 0.5 * a
   x.append(r * math.cos(a))
   y.append(r * math.sin(a))
plt.plot(x, y, color='blue', label="Спираль Архимеда")

ax.set_xlabel('X-axis', fontname='Impact', fontsize=14)
ax.set_ylabel('Y-axis', fontname='Impact', fontsize=14)

ax.set_title('Графики функции: СПИРАЛЬ АРХИМЕДА', fontname='Impact')
ax.grid(True)

fig.patch.set_facecolor('#BC8F8F')
ax.set_facecolor('#FFFFE0')
plt.legend(loc='upper left', frameon=True, fontsize=8, title='Легенда')

plt.show()

