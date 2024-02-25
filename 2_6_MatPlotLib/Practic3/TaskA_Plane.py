# Для создания 3D графиков и визуализаций в Matplotlib вы можете использовать модуль mplot3d.
# Вот примеры создания 3D графиков и работы с трехмерными данными:

# График поверхности:
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np

# Создаем данные для графика поверхности
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))
# Создаем фигуру и 3D оси
fig = plt.figure()
ax = plt.axes(projection='3d')
# Создаем график поверхности
ax.plot_surface(X, Y, Z, cmap='viridis')
# Добавляем метки осей
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
# Отображаем график
plt.show()
