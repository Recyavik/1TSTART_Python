# Постройте круговую диаграмму в левой части фигуры, содержащую процентное отношение
# каждой породы собак к общему числу участников выставки животных согласно,
# представленных списков. А в правой части фигуры разместите столбчатую диаграмму
# количества кошек и собак, которые участвовали в трёх номинациях 'BEST', 'FAST', 'BIG'.
# Сохраните полученный график в формате: png, pdf и svg.


import matplotlib.pyplot as plt
import numpy as np

dogs = ['Спаниель', 'Дог', 'Бигль', 'Босерон', 'Гампр', 'Кангал', 'Такса']
numbers = [15, 20, 11, 9, 4, 5, 17]
explode = (0, 0.1, 0, 0, 0, 0, 0)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.title("Процент участия по пародам собак", fontsize=12, fontweight="bold", color="blue")
plt.pie(numbers, explode=explode, labels=dogs, autopct='%1.1f%%', startangle=60)
plt.axis('equal')


plt.subplot(1,2,2)
width = 0.4
cat_numbers = [12, 15, 20]
dog_numbers = [13, 14, 11]
competition_list = ['BEST', 'FAST', 'BIG']
x_indexes = np.arange(len(competition_list))
plt.xticks(x_indexes, competition_list)
plt.title("Конкурс питомцев", fontsize=12, fontweight="bold", color="green")
plt.xlabel("Номинации", fontsize=10, color="green")
plt.ylabel("Количество", fontsize=10, color="green")
plt.bar(x_indexes - (width/2), cat_numbers, label='Кошки" ', width=width, color="OrangeRed")
plt.bar(x_indexes + (width/2), dog_numbers, label='Собаки" ', width=width, color="Gold")
ax = plt.gca()
ax.set_facecolor("MistyRose")
plt.legend()
plt.grid()
plt.savefig('graf.png', dpi=300)  # указываем имя файла и разрешение (dpi)
plt.savefig('graf.pdf')
plt.savefig('graf.svg')

plt.show()