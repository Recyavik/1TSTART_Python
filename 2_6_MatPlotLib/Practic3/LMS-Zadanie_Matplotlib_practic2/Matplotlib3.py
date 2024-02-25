# Постройте анимированную функцию красного цвета из 60 кадров для косинуса от -2π до π.
# Настройте лимиты, чтобы хорошо было видно максимум и минимум функции на сетке графика.
# Запишите анимацию в файл в формате gif.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'ro')


def init():
    ax.set_xlim(-2*np.pi, 2*np.pi)
    ax.set_ylim(-1.1, 1.1)
    return ln,

def update(frame):
    xdata.append(frame)
    ydata.append(np.cos(frame))
    ln.set_data(xdata, ydata)
    return ln,
plt.grid()

ani = FuncAnimation(fig, update, frames=np.linspace(-2*np.pi, 2*np.pi, 60),
                    init_func=init, blit=True)

ani.save('animation.gif')
plt.show()