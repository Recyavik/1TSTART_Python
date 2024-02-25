# Модуль числа
a = int(input("Модуль какого числа хотите найти?  "))
if a < 0:
    a = - a
print(f"Модуль числа = {a}")

# Анализ возраста
age = int(input("Введите возраст:"))
if age == 14:
   print("В этом году вы сможете получить паспорт")
else:
   print("Прекрасный возраст!")

# Чётные и не чётные числа
value = int(input('Введите любое число: '))
if value % 2 == 0:
   print(f'Число {value} - чётное ')
else:
   print(f'Число {value} - нечётное ')

# Чётные и не чётные числа (инверсия условия)
value = int(input('Введите любое число: '))
if  value % 2 != 0:
   print(f'Число {value} - нечётное ')
else:
   print(f'Число {value} - чётное ')

# Сравнение чисел
a = 5
b = 5
if a < b:
   print(f'Число {a} меньше {b} ')
elif a == b:
   print(f'Число {a} равно {b}')
else:
   print(f'Число {a} больше {b}')

# Вложенные условия (максимальное из трёх чисел)
a = 3
b = 5
c = 2

if a > b:
   if a > c:
      print("a -> max")
   else:
      print("c -> max")
else:
   if b > c:
      print("b -> max")
   else:
      print("c -> max")
