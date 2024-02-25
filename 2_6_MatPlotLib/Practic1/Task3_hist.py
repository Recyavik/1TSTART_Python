# Гистограмма:
import matplotlib.pyplot as plt

# Задаем данные
data = [1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 5]
x = list(range(1, 6))
plt.xticks(x)
# Создаем гистограмму
plt.hist(data)
# Добавляем подписи осей и заголовок
plt.xlabel('Значение')
plt.ylabel('Частота')
plt.title('Пример гистограммы')
# Отображаем график
plt.show()
