product_name = input("Введите название товара: ")
price = input("Введите цену товара: ")
count = input("Введите количество товара: ")
cost = count * price
print("Стоимость = ", cost)
print(product_name, '-', type(product_name))
print(price, '-', type(price))

price = float(input("Введите цену товара: "))
print(price, '-', type(price))
count = 5
cost = count * price
print("Стоимость = ", cost)

### Список арифметических операций над числами
#       + сложение					c = 5 + a,  для с  = 5 + a
#       - вычитание					c = 5 - a,  для с = 5 - a
#       * умножение					c = 5 * a,  для с = 5a
#       ** степень 					c = 5 ** 3, для с = 53
#       / деление					с = 5 / 2, для с = 5 : 2
#       // целочисленное деление 		с = 5 // 3, для с = 1
#       % остаток от деления			с = 5 % 3, для с = 2

a = 1458
print(a // 100)
print(a % 100)

# Два способа поменять местами переменные

