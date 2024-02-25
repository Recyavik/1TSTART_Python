# Задание Классы 4
# Создайте класс House.
# # Добавьте в класс атрибуты is_roof_created и is_walls_created. Для данных атрибутов установите значение False
# в классе House.
# Добавьте в класс метод create_walls, который выводит в консоль сообщение "Построили стены"
# и меняет значение атрибута is_walls_created на True .
# Добавьте в класс метод create_roof, который выводит в консоль сообщение "Построили крышу"
# и меняет значение атрибута is_roof_created на True . Обратите внимание, что построить крышу,
# можно только если атрибут is_walls_created равен True. Если построить крышу не представляется возможным,
# то выведите в консоль сообщение "Нельзя построить крышу".
#
# Добавьте в класс метод create_house, который выводит в консоль сообщение "Построили дом".
# Обратите внимание, что построить дом, можно только если значение атрибута is_roof_created равен True.
# Если построить крышу не представляется возможным, то выведите в консоль сообщение "Нельзя построить дом".

# Создайте экземпляр класса House.
# Вызовите метод постройки стен у созданного экземпляра.
# Вызовите метод постройки крыши у созданного экземпляра.
# Вызовите метод постройки дома у созданного экземпляра.

"""
Пример вывода в консоль:
Построили стены
Построили крышу
Построили дом
""" #

class House:
    is_roof_created = False
    is_walls_created = False

    def create_walls(self):
        print('Построили стены')
        self.is_walls_created = True

    def create_roof(self):
        if self.is_walls_created == True:
            print('Построили крышу')
            self.is_roof_created = True
        else:
            print('Нельзя построить крышу раньше стен')

    def create_house(self):
        if self.is_walls_created == True and  self.is_roof_created == True:
            print('Построили дом')
        elif self.is_roof_created == False and self.is_walls_created == True:
             print('Нельзя построить дом раньше крыши')
        elif self.is_roof_created == True and self.is_walls_created == False:
             print('Нельзя построить дом раньше стен')
        else:
            print('Нельзя построить дом')


house1 = House()
house1.create_house()
house1.create_walls()
house1.create_house()
house1.create_roof()
house1.create_house()

