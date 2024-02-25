import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
# Создаем данные для трехмерного рассеяния
np.random.seed(123)
num_points = 100
x = np.random.normal(0, 1, num_points)
y = np.random.normal(0, 1, num_points)
z = np.random.normal(0, 1, num_points)
c = np.random.rand(num_points)  # цвета точек
# Создаем фигуру и 3D оси
fig = plt.figure()
ax = plt.axes(projection='3d')

# Создаем трехмерное рассеяние

ax.scatter3D(x, y, z, c=c, cmap='cool')

# Добавляем метки осей
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
# Отображаем график
plt.show()
