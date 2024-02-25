def sum_student(name, *scores):
    data = list()
    print(f'Ученик: {name} набрал:', end=' ')
    for el in scores:
        print(f'{el}',end=' ')
        data.append(el)
    print('баллов = ', sum(scores))
    return data, sum(scores)

all_data = sum_student('Артём', 10, 12, 30, 45)
print(all_data)
(list_data, s) = all_data
print('Список баллов = ', list_data)
print('Общая сумма = ', s)


all_data = sum_student('Артём', 1, 2, 3, 4)
print(all_data)


def printPetNames(flat, **pets):
   print(f"В квартире: {flat}")
   for pet, name in pets.items():
      print(f"{pet}: {name}")

printPetNames(45, dog="Бимка", cat=["Мурка", "Барсик", "Молли"], turtle="Ракета")

# Конструкцию **kwargs нельзя располагать до *args. Если это сделать — будет выдано сообщение об ошибке.