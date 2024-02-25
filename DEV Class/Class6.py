# Задание Классы 6
# Создайте класс Human с атрибутом name.
#
# Создайте конструктор __init__(self).  В конструкторе запросите имя человека и задайте значение атрибута name
# согласно введенному значению.
# Добавьте в класс метод Eat(), который будет выводить в консоль строку вида: name is eating.
#
# Добавьте в класс метод Sleep(), который будет выводить в консоль строку вида: name is sleeping.
# Добавьте в класс метод Work(), который будет выводить в консоль строку вида: name is working.
#
# Создайте объект класса Human.
# Задайте ему значение имени.
# Вызовите метод Eat() у созданного объекта.
# Вызовите метод Sleep() у созданного объекта.
# Вызовите метод Work() у созданного объекта.

"""
Пример вывода:
Введите имя человека: Михаил
Михаил is eating.
Михаил is sleeping.
Михаил is working.
""" #

class Human:
    name = None
    def __init__(self):
        self.name = input('Как вас зовут: ')

    def Eat(self):
        print(f'{self.name} is eating.')

    def Sleep(self):
        print(f'{self.name} is sleeping.')

    def Work(self):
        print(f'{self.name} is working.')

h = Human()
# h.name = 'Михаил'
h.Eat()
h.Sleep()
h.Work()
