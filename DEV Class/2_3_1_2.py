# Напишите функцию get_user_data() для запроса следующих  данных от пользователя:
# ФИО, Почта, Номер телефона. Создайте переменные name, email, number и при помощи метода input
# запросите в них значения. Используйте метод print для вывода введенных вами значений.
# Вывод должен содержать:
"""
ФИО: Ваш Input
Почта: Ваш Input
Номер телефона: Ваш Input
""" #

def get_user_data():
    name = input('Введите ФИО: ')
    email = input('Введите почту: ')
    number = input('Введите номер телефона: ')
    return name, email, number

name, email, number = get_user_data()
print('ФИО:',name)
print('Почта:',email)
print('Номер телефона:',number)
