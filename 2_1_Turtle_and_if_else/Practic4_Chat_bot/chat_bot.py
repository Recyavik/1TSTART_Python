name = input('Как вас зовут?')
surname = input('Какое у вас отчество?')
fam = input('Какая у вас фамилия?')
age = int(input("Сколько вам лет?: "))
fio = f'{fam.strip()} {name.strip()} {surname.strip()}'.title()
print('Очень приятно, ', fio)
print(f"Не заметишь как вам уже {age+1}")



age = 0
height = 0
weight = 0

print("Здравствуйте")
firstname = input("Как тебя зовут: ")
if len(firstname) == 0:
    print("Попробуем еще раз ввести имя ")
    firstname = input("Как тебя зовут: ")
print(firstname, " - красивое имя!")

consent = input("Я могу узнать твою фамилию. Ответь да/нет ")
if consent == "Да" or consent == "да" or consent == "ДА":
    print("Супер!")
    surname = input("Введите свою фамилию :")
    if len(surname) == 0:
        print("Попробуем ввести еще раз")
        surname = input("Введите свою фамилию :")
    else:
        print("Отличное сочетание с именем: ", firstname, surname)
else:
    print("Ладно, давай в другой раз...")
    surname = "Не зафиксирована"

a = input("Сколько тебе лет," + firstname + "?")
if a.isdigit():
    age = int(a)
    if age < 7:
        print("Не заметишь ка тебе уже" + str(age+1))
    elif 7 <= age < 18:
        print("Значит ты учишься в школе")
    elif 18 <= age < 25:
        print("Молодость - это прекрасно!")
    elif 25 <= age < 45:
        print("Значит у тебя много жизненного опыта")
    elif 45 <= age <= 90:
        print("Ты мудры человек")
    else:
        print("Не вероятный возраст!")
else:
    print("Даже так?")

hobby = input("Чем ты любишь заниматься," + firstname)
print("Здорово!")

consent = input("Могу я узнать твой рост и вес? Ответь да/нет")
if consent.title() == "Да":
    print("Спасибо, отлично!")
    h = input("Какой у тебя рост? ")
    w = input("Какой у тебя вес? ")
    if h.isdigit():
        height = float(h)
        print("Спасибо, зафиксировано")
    if w.isdigit():
        weight = float(w)
        print("Спасибо, зафиксировано")
else:
    print("Хорошо, давай в другой раз....")

print("Зафиксированы данные:")
print("Имя:", firstname)
print("Фамилия:", surname)
print("Возраст:", age)

if height > 0:
    print("Рост:", height)
else:
    print("Рост:", "не зафиксирован")

if weight > 0:
    print("Вес:", weight)
else:
    print("Вес:", "не зафиксирован")
