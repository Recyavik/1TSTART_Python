# Задание Классы 1
# Cоздайте класс "Person". Создайте метод класса introduce(self, name, age) принимающий введенные с клавиатуры значения
# имени и возраста. В методе используйте динамическое добавление атрибутов name и age в объект класса Person.
# Метод должен вывести в консоль строку вида: “Привет, меня зовут _name, мне _age лет.”
# Вместо _name и _age должны находиться данные введенные с клавиатуры.
# При обращении к атрибутам класса используйте self. Не забудьте создать экземпляр класса.

class Person:
    def __init__(self, name: str ='Не задано', age: int =0):
        self.name = name
        self.age = age

    def input_data(self):
        self.name = input('Введите ваше имя: ')
        self.age = int(input('Введите ваш возраст: '))
        return self.name, self.age

    def introduce(self, name, age):
        print(f'Привет, меня зовут {name}, мне {age} лет.')

men = Person()
men.input_data()
men.introduce(men.name, men.age)