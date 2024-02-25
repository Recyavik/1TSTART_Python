# Создайте Series структуры из трех типов данных (словаря, списка и линейного массива numpy).
# Покажите часть каждой структуры (от первого элемента до 5).
# Покажите в консольном экране результат среза, затем удалите методом в полученной структуре только последний
# и предпоследний элемент и снова покажите элементы оставшейся структуры.
# Вычислите основные статистические показатели Series (среднее, стандартное отклонение, минимум, максимум)

import pandas as pd
import numpy as np

numbers_list = [11, 22, 33, 44, 55, 66, 77, 88, 99, 101]
week_dict = {1:'Понедельник', 2:'Вторник', 3:'Среда', 4: 'Четверг', 5: 'Пятница', 6: 'Суббота', 7:'Воскресенье'}
line_numpy = np.linspace(0, 1, 15)

print('Исходные данные в формате структуры Series')
s_from_list = pd.Series(numbers_list)
print(s_from_list)
s_from_dict = pd.Series(week_dict)
print(s_from_dict)
s_from_np = pd.Series(line_numpy)
print(s_from_np)
print('--------------------------------------------')

print('Срез первых пяти элементов')
for el in [s_from_list, s_from_dict, s_from_np]:
    print(el[:5])
print('--------------------------------------------')

print('Удаление двух последних элементов')
for el in [s_from_list, s_from_dict, s_from_np]:
    count = el.count()
    if sum(el.head(1).index) == 0:
        count = count - 1
    el = el.drop(count)
    el = el.drop(count-1)
    print(el)
    print(el.describe())
    print('--------------------------------------------')
