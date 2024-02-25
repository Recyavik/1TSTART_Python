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

"""  #
from datetime import datetime

class Athletes:

    def __init__(self, name, born_year):
        self.name = name
        self.born_year = born_year
        today = datetime.now()
        # today = f'{today: %d.%m.%Y}'
        today = int(f'{today:%Y}')
        self.age = today - self.born_year
        self.__series = '00 00'
        self.__number = '000000'

    def get_series_number(self):
        return self.__series, self.__number

    def set_series_number(self, series, number):
        self.__series = series
        self.__number = number

    def info(self):
        print('Анкета спортсмена:')
        print(f'ФИО: {self.name}')
        print(f'Год рождения: {self.born_year}')
        print(f'Возраст: {self.age}')

    def info_admin(self):
        self.info()
        print(f'Паспорт: {self.__series} {self.__number}')
        print()


    def check(self):
        flag = True
        self.name = self.name.title()
        if self.age < 0:
            print('Не корректная дата рождения')
            self.born_year = int(input(f'Спортсмен - {self.name}, введите его год рождения: '))
            today = datetime.now()
            today = int(f'{today:%Y}')
            self.age = today - self.born_year
        if self.age < 0:
            flag = False

        if len(self.__series) !=5 or self.__series[2] != ' ' or self.__series.isalpha():
            print('Не корректная серия документа')
            self.__series = input(f'{self.name}: Введите серию паспорта из 5 цифр с пробелом: ')
        if len(self.__series) != 5 or self.__series[2] != ' ' or self.__series.isalpha():
            flag = False


        if len(self.__number) !=6 or self.__series.isalpha():
            print('Не корректный номер документа')
            self.__number = input(f'{self.name}: Введите паспорта паспорта из 6 цифр: ')
        if len(self.__number) !=6 or self.__series.isalpha():
            flag = False


        return flag

    def save_anketa(self, path='sport.txt'):
        with open(path, 'a') as file:
            if self.check():
                anketa = []
                anketa.append(self.name + '\n')
                anketa.append(str(self.born_year) + '\n')
                anketa.append(self.__series + '\n')
                anketa.append(self.__number + '\n')

                file.writelines(anketa)


s1 = Athletes('Иванов Иван иванович', 2998)
s2 = Athletes('Иванов Сергей Иванович', 1997)
s1.set_series_number('25 16', '112233')
s2.set_series_number('25 17', '775599')
s3 = Athletes('Петров Петр Петрович', 2000)
s3.set_series_number('11 12', '777777')

for el in [s1, s2, s3]:
    el.save_anketa()
    el.info_admin()

