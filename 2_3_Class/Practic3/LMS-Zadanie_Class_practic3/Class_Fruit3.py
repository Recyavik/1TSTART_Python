# Создайте класс для описания шин - Tire. Унаследуйте от этого класса все атрибуты:
# производитель, размер шины, сезон для новых классов BikeTire, CarTire, и базовый метод fitting, т.е. шиномонтаж.
# Воспользуйтесь декораторами, чтобы создать доступ к свойству – давление в шинах.
# Обеспечивайте валидность этого свойства для автомобильных шин
# (давление не должно превышать 3.5 атмосфера и не должно быть меньше 1.5),
# а для велосипедных шин (давление не должно превышать 3.4 атмосфера и не должно быть меньше 2.3).
# Покажите на примерах работу базовой функции "шиномонтаж" и функцию экземпляра класса подкачки шин - inflate_tire.
# Покажите возможность обращения к свойствам атрибутов класса с проверкой на валидность давления.

import random as rnd


class Tire:

    def __init__(self, maker, size, season):
        self.maker = maker
        self.size = size
        self.season = season
        self.__bp = 0

    @classmethod
    def fitting(cls):
        print('Произведен шиномонтаж!')


class BikeTire(Tire):

    def __init__(self, maker, size, season):
        super().__init__(maker, size, season)
        self.maker = maker
        self.size = size
        self.season = season
        self.__bp = 0

    @property
    def bp(self):
        return self.__bp

    @bp.setter
    def bp(self, b):
        if 2.3 <= b <= 3.4:
            self.__bp = b
        else:
            raise ValueError

    @bp.deleter
    def bp(self):
        del self.__bp

    def inflate_tire(self, b):
        super().fitting()
        self.bp = b
        self.info()

    def info(self):
        print(f'Велосипедная шина: {self.size}, {self.maker}, {self.season}, давление в шине = {self.bp} \n')


class CarTire(Tire):

    def __init__(self, maker, size, season):
        super().__init__(maker, size, season)
        self.maker = maker
        self.size = size
        self.season = season
        self.__bp = 0

    def inflate_tire(self, b):
        super().fitting()
        self.__bp = b
        self.info()

    @property
    def bp(self):
        return self.__bp

    @bp.setter
    def bp(self, b):
        if 2.3 <= b <= 3.4:
            self.__bp = b
        else:
            raise ValueError

    @bp.deleter
    def bp(self):
        del self.__bp

    def info(self):
        print(f'Автомобильная шина: {self.size}, {self.maker}, {self.season}, давление в шине = {self.bp} \n')


maker_list = ['Cordiant', 'Roadcruza', 'ЯШЗ', 'УралШина', 'ОмскШина', 'YOKOHAMA']
size_bike_list = [12, 16, 18, 20, 24, 26, 27.5, 28, 29]
size_car_list = [14, 15, 16, 17, 18, 19, 20, 21, 22]
season_list = ['Summer', 'Winter']
rnd.seed()
s1 = CarTire(rnd.choice(maker_list), rnd.choice(size_car_list), rnd.choice(season_list))
s1.info()
s1.inflate_tire(2)
# s1.bp = 4
s1.bp = 3
s1.info()

s2 = CarTire(rnd.choice(maker_list), rnd.choice(size_car_list), rnd.choice(season_list))
s2.inflate_tire(2.5)
s1.bp = 2.8
s1.info()

b1 = BikeTire(rnd.choice(maker_list), rnd.choice(size_bike_list), rnd.choice(season_list))
b1.inflate_tire(3.1)
