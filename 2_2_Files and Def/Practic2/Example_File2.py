import csv

# with open('Книга1.csv', encoding='utf-8') as file:
#     data = csv.reader(file, delimiter=';')
#     count = 0
#     for row in data:
#         if count == 0:
#             print(f'Файл содержит столбцы: {','.join(row)}')
#         else:
#             print(f'  {row[0]} - {row[1]}: этот человек родился в {row[2]} году')
#         count +=1
#     print(f'Всего в файле {count}')
#

with open('classmates55.csv', mode='w') as file:
    names = ['Имя', 'Возраст']
    data_writer = csv.DictWriter(file, delimiter=',',
                                 lineterminator='\r', fieldnames=names)
    data_writer.writeheader()
    data_writer.writerow({'Имя': 'Глаша', 'Возраст': '14'})
    data_writer.writerow({'Имя': 'Маша', 'Возраст': '15'})
    data_writer.writerow({'Имя': 'Арина', 'Возраст': '13'})

