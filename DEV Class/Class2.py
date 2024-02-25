# Создайте класс “Person”. В данном классе реализуйте методы greet и celebrate_birthday.
# Метод greet должен возвращать строку вида: "Привет, меня зовут name".
# Метод celebrate_birthday должен возвращать строку вида: "Мне age лет".
# Атрибуты name и age являются динамическими, объявлять в классе их не надо.
# Созданный класс расположите на месте троеточия как представлено в шаблоне кода.
""" 
Пример вывода:
Привет, меня зовут Михаил.
Мне 16 лет.
""" #

class Person:
    def __init__(self, name='Неизвестно', age=None):
        self.name = name
        self.age =None

    def greet(self):
        return f"Привет, меня зовут {self.name}."

    def celebrate_birthday(self):
        return f"Мне {self.age} лет."
#TODO здесь создайте класс
person = Person()
person.name = "Михаил"
person.age = 16
print(person.greet())
print(person.celebrate_birthday())