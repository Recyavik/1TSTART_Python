from matplotlib import pyplot as plt



expenses = ['Питание', 'Развлечение', 'ЖКХ', 'Одежда', 'Транспорт']
money = [15_000, 5_000, 8_000, 9_000, 4_000]
explode = (0.1, 0, 0, 0, 0)

fig1, ax1 = plt.subplots()
ax1.pie(money, explode=explode, labels=expenses, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')

plt.show()
