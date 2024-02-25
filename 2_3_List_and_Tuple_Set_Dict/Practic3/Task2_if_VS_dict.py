# month_line = ""
# month = int(input('Введите номер месяца:'))
# if month == 1:
#     month_line = 'Январь'
# elif month == 2:
#     month_line = 'Февраль'
# elif month == 3:
#     month_line = 'Март'
# elif month == 4:
#     month_line = 'Апрель'
# elif month == 5:
#     month_line = 'Май'
# elif month == 6:
#     month_line = 'Июнь'
# elif month == 7:
#     month_line = 'Июль'
# elif month == 8:
#     month_line = 'Август'
# elif month == 9:
#     month_line = 'Сентябрь'
# elif month == 10:
#     month_line = 'Октябрь'
# elif month == 11:
#     month_line = 'Ноябрь'
# elif month == 12:
#     month_line = 'Декабрь'
# else:
#    print('Невозможно определить!')
# print(month_line)


months = ({1: "Январь", 2:"Февраль", 3: "Март", 4: "Апрель", 5: "Май", 6: "Июнь", 7: "Июль", 8: "Август",
           9: "Сентябрь", 10: "Октябрь", 11: "Ноябрь", 12: "Декабрь "})
key = int(input("Введите номер месяца: "))
try:
    print(months[key])
except (KeyError):
    print('Невозможно определить!')


