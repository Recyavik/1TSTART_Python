"""
Класс Athletes содержит шаблон анкетных данных о спортсмене:
 ФИО
 год рождения
 возраст спортсмена 
 серию и номер паспорта (скрыты от доступа и проверяются по длине)
 
Класс обладает способностью выводить информацию о спортсменах 
и проверять анкетные данные на валидность
Так же класс способен записывать только качественно внесенные данные в файл: 'sport.txt'
добавляя к уже существующему файлу новых спортсменов

""" #
from datetime import datetime

class Athletes:


    def __init__(self, name, born_year):
        self.name = name
        self.born_year = born_year
        today = f'{datetime.now():%Y}'
        # today = f'{datetime.now():%d.%m.%Y}'
        self.age = int(today) - self.born_year
        self.__series = '00 00'
        self.__number = '000000'

    def get_serial_number(self):
        return self.__series, self.__number

    def set_serial_number(self, seral, number):
        self.__series = seral
        self.__number = number

    def info(self):
        print('Анкета спортсмена:')
        print(f'ФИО: {self.name}')
        print(f'Год рождения: {self.born_year}')
        print(f'Возраст: {self.age}')

    def info_admin(self):
        self.info()
        print(f'Паспорт: {self.__series} {self.__number}')



    def check(self):
        flag = True
        self.name = self.name.title()
        if self.age < 0:
            print('Не корректная дата рождения')
            self.born_year = int(input(f'Cпортсмен - {self.name}, введите его год рождения: '))
            today = f'{datetime.now():%Y}'
            self.age = int(today) - self.born_year
        if self.age < 0:
            flag = False
        if len(self.__series) != 5 or self.__series[2] != ' ':
            print('Не корректная серия документа')
            self.__series = input('Введите серию паспорта из пяти символов c пробелом:')
        if len(self.__series) != 5 or self.__series[2] != ' ':
            flag = False
        if len(self.__number) != 6 or self.__number.isalpha():
            print('Не корректный номер документа')
            self.__number = input('Введите номер документа из шести цифр')
        if len(self.__number) != 6 or self.__number.isalpha():
            flag = False
        return flag

    def save(self, path='sport.txt'):
        with open(path, 'w') as file:
            if self.check():
                anketa = []
                anketa.append((self.name + '\n'))
                anketa.append(str(self.born_year) + '\n')
                anketa.append((self.__series + '\n'))
                anketa.append((self.__number + '\n'))

                file.writelines(anketa)

s1 = Athletes('Иванов иван иванович', 1999)
s1.set_serial_number('25 16', '777777')


s2 = Athletes('Петров Петр Петрович', 2005)
s2.set_serial_number('2517', '888888')


for el in [s1, s2]:
    el.check()
    el.info_admin()
    el.save()



