# Создайте класс Fruit (фрукты) и класс Vegetables (овощи). У каждого класса есть функция роста,
# атрибуты: размер, цвет и статус готовности для сбора.  Используйте конструктор чтобы каждый экземпляр
# фрукта обладал названием, цветом, и статусом готовности для сбора этого фрукта.
# Создайте 2 любых экземпляра фруктов и 3 экземпляра для овощей с этими атрибутами.
# Запустите функцию роста для каждого экземпляра класса с параметром увеличения размера.
# Статус готовности к сбору урожая будет зависеть от этого размера.
# Как только размер станет больше 10 сантиметров, его статус поменяется.
# При создании инкапсулируйте размеры фруктов и овощей. Продемонстрируйте работу функций на своих примерах.

class Fruit:

    def __init__(self, name='фрукт', color='неизвестно', status=False):
        self.name = name
        self.color = color
        self.status = status
        self.__size = 0

    def get_size(self):
        return self.__size

    def set_size(self, r):
        self.__size = r
        print(f'У фрукта: {self.name} зафиксированы новые размеры = {r}')

    def growth(self, delta_size):
        print(f'Фрукт: {self.name} вырос на {delta_size} см.')
        self.__size += delta_size
        if self.__size > 10:
            self.status = True

    def info(self):
        if self.status:
            print(f'Фрукт: {self.name} {self.color} поспел до размеров {self.__size} см. и к сбору готов!')
        else:
            print(f'Фрукт: {self.name} {self.color} вырос до размеров {self.__size} см. и к сбору не готов')


class Vegetables:

    def __init__(self, name='овощ', color='неизвестно', status=False):
        self.name = name
        self.color = color
        self.status = status
        self.__size = 0

    def get_size(self):
        return self.__size

    def set_size(self, r):
        self.__size = r
        print(f'У овоща: {self.name} зафиксированы новые размеры = {r}')

    def growth(self, delta_size):
        print(f'Овощ: {self.name} вырос на {delta_size} см.')
        self.__size += delta_size
        if self.__size > 10:
            self.status = True

    def info(self):
        if self.status:
            print(f'Овощ: {self.name} {self.color} поспел до размеров {self.__size} см. и к сбору готов!')
        else:
            print(f'Овощ: {self.name} {self.color} вырос до размеров {self.__size} см. и к сбору не готов')


f1 = Fruit('Яблоко')
f2 = Fruit('Персик', 'желтый')
v1 = Vegetables('Помидор', 'зеленый', False)
v2 = Vegetables('Огурец', 'зеленый', False)
v3 = Vegetables('Лук')


f1.growth(5)
size_f1 = f1.get_size()
print(f'Размер {f1.name} = {size_f1}')

for el in [f1, f2, v1, v2, v3]:
    el.growth(5)
    el.info()

f2.set_size(10)
v1.color = 'red'

for el in [v1, v2, v3]:
    el.growth(6)
    el.info()
