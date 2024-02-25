# Точечный график:

import matplotlib.pyplot as plt
# Задаем данные
x2 = list(range(-15, 16))
y2 = [el**3 for el in x2]

# Создаем точечный график
plt.scatter(x2, y2)
# Добавляем подписи осей и заголовок
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Пример точечного графика')
# Отображаем график
plt.show()
