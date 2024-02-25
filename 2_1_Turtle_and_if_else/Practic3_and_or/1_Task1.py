""" 
if условие:
	место для команд, которые выполнятся, 
	если условие истинно
	...........
else:
    место для команд, которые выполнятся, 
    если все выше представленные условия ложны
    ..........
""" #
"""
if 1-ое условие:
	место для команд, которые выполнятся, если условие истинно
	...........
if 2-ое условие:
	место для команд, которые выполнятся, 
	если 1-ое условие ложно, a 2-ое истинно
	...........
if 3-е условие:
	место для команд, которые выполнятся, 
	если 1-ое и 2-ое условие ложно, 
	a 3-е истинно
	...........
else:
    место для команд, которые выполнятся, 
    если все выше представленные условия ложны
    .......... 
""" #

month = int(input("Введите номер месяца"))
if month == 1:
    print("Январь")
elif month == 2:
    print("Февраль")
elif month == 3:
    print("Март")
elif month == 4:
    print("Апрель")
elif month == 5:
    print("Май")
elif month == 6:
    print("Июнь")
elif month == 7:
    print("Июль")
elif month == 8:
    print("Август")
elif month == 9:
    print("Сентябрь")
elif month == 10:
    print("Октябрь")
elif month == 11:
    print("Ноябрь")
elif month == 12:
    print("Декабрь")
else:
    print("Не могу определить")


""" 
ИНВЕРСИЯ (ЛОГИЧЕСКОЕ  ОТРИЦАНИЕ) not - "НЕ"
0 - False
1 - True

не 0 = 1
не 1 = 0

if not условие:
	место для команд, которые выполнятся, 
	если условие истинно
	...........
else:
    место для команд, которые выполнятся, 
    если все выше представленные условия ложны
    ..........
""" #
a = 5
if not a == 5:
    print("Обычный ученик!")
else:
    print("Отличник!")

a = 5
if a != 5:
    print("Ообычный ученик!")
else:
    print("Отличник!")

"""
КОНЪЮНКЦИЯ (ЛОГИЧЕСКОЕ  УМНОЖЕНИЕ) and - "И"
A and B = F       A * B = F
-----------------------------------
0 and 0 = 0       0 * 0 = 0
0 and 1 = 0       0 * 1 = 0
1 and 0 = 0       1 * 0 = 0
1 and 1 = 1       1 * 1 = 1
# Общее условие = ИСТИНА только когда оба условия равны 1 - ИСТИНА
""" #
"""
if условие-A and условие-B:
	место для команд, которые выполнятся, 
	если условие A и B (оба условия) истинны
	...........
else:
    место для команд, которые выполнятся, 
    если хотя бы одно из условий (A, B) ложны
    ..........
""" #

month = 3
if month >2 and month <= 5:
   print(month,'- это весенний месяц')
else:
   print(month,'- это точно не весна')

month = 3
if  2 < month <= 5:
   print(month,'- это весенний месяц')
else:
   print(month,'- это точно не весна')

# Средний балл
a, b, c, d = map(int, input("Введите четыре оценки через пробел: ").split())
sr_ball = (a + b + c + d) / 4

print("Средний балл = %4.2f" % sr_ball)
if sr_ball >= 4.6 and sr_ball <= 5:
    print("Оценка - 5!")

elif sr_ball >= 3.6 and sr_ball < 4.6:
    print("Оценка - 4")

elif 2.6 < sr_ball < 3.6:
    print("Оценка - 3")

elif 2 < sr_ball <= 2.6:
    print("Оценка - 2")

else:
    print("Невозможно определить оценку!")

"""
ДИЗЪЮНКЦИЯ (ЛОГИЧЕСКОЕ  СЛОЖЕНИЕ) or - "ИЛИ"
A or B = F       A + B = F
-----------------------------------
0 or 0 = 0       0 + 0 = 0
0 or 1 = 1       0 + 1 = 1
1 or 0 = 1       1 + 0 = 1
1 or 1 = 1       1 + 1 = 1
Общее условие будет ИСТИНА, если хотя бы одно из условий будет истинно
""" #
"""
if условие-A or условие-B:
	место для команд, которые выполнятся, 
	если одно из условий A или B истинно
	...........
else:
    место для команд, которые выполнятся, 
    если оба условия (A, B) ложны
    ..........
""" #

month = 12
if month == 12 or month == 1 or month == 2:
   print(month,'- это зимний месяц')
else:
   print(month,'- это точно не зима')

month = int(input('Введите номер месяца:'))
if month == 12 or 1 <= month <= 2:
    season = 'Зима'
elif 3 <= month <= 5:  # Или можно записать так: month >= 3 and month <= 5
    season = 'Весна'
elif 6 <= month <= 8:  # Или можно записать так: month >= 6 and month <= 8
    season = 'Лето'
elif 9 <= month <= 11: # Или можно записать так: month >= 9 and month <= 12
    season = 'Осень'
else:
    season = 'Невозможно, вы ошиблись при вводе номера месяца'

print(month,'месяц - это: ',season)

