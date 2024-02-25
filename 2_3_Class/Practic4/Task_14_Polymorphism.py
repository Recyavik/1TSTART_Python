# В буквальном значении полиморфизм означает множество форм.
# Полиморфизм — очень важная идея в программировании.
# Она заключается в использовании единственной сущности(метод, оператор или объект)
# для представления различных типов в различных сценариях использования.

# Море волнуется раз.

# Полиморфизм — когда наследники делают все по своему, но результат работы такой же как у базового класса.
# Если наследник занимается чем-то своим и не дает результат такой, который ожидается от базового
# класса — значит с наследованием и полиморфизмом что-то не так.
# Пример: есть базовый класс автомобиль, который предположительно должен заехать в гараж.
# Создаем летающий автомобиль-наследник (как в фильме «Назад в будущее 2»).
# Какой будет результат при попытке загнать этого монстра в гараж?
# Да, он может залететь в гараж, если функция езды будет полностью заменена на функцию полета.
# А если функция полета была новым функционалом, а функция езды вообще заблокирована?
# То мы не сможем спрятать нашего летуна от непогоды.
# Это уже не будет автомобиль, это будет что-то новое.
# Результат — из-за неправильного моделирования и наследования был нарушен принцип полиморфизма
# и получился нежелательный результат.


# Мы знаем, что оператор + часто используется в программах на Python. Но он не имеет единственного использования.
# Для целочисленного типа данных оператор + используется чтобы сложить операнды.

num1 = 1
num2 = 2
print(num1 + num2)

num1 = "1"
num2 = "2"
print(num1 + num2)

# Здесь мы можем увидеть единственный оператор + выполняющий разные операции для различных типов данных.
# Это один из самых простых примеров полиморфизма в Python.

print(len("Python"))
print(len(["Python", "Java", "C"]))
# В Python есть некоторые функции, которые могут принимать аргументы разных типов.
# Одна из таких функций — len(). Она может принимать различные типы данных.
# Давайте посмотрим на примере, как это работает.

# Полиморфизм — очень важная идея в объектно-ориентированном программировании.
# Мы можем использовать идею полиморфизма для методов класса,
# так как разные классы в Python могут иметь методы с одинаковым именем.

# Такой пример мы уже рассматривали, но не оговаривали, что он скрывает парадигму полиморфизма
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def make_sound(cls):
        print("Животное издаёт звук:")


class Cat(Animal):
    def make_sound(self):
        super().make_sound()
        print(self.name, "Мяу")


class Dog(Animal):
    def make_sound(self):
        super().make_sound()
        print(self.name, "Гав")


cat1 = Cat("Мурзик", 3)
cat2 = Cat("Барсик", 2)
cat3 = Cat("Коша", 1)

dog1 = Dog("Шарик", 5)
dog2 = Dog("Бимка", 2)
dog3 = Dog("Ирма", 4)


list_obj = [cat1, dog1, cat2, cat3, dog2, dog3]
for el in list_obj:
    el.make_sound()

# Как и в других языках программирования, в Python дочерние классы могут наследовать методы
# и атрибуты родительского класса. Мы можем переопределить некоторые методы и атрибуты специально
# для того, чтобы они соответствовали дочернему классу, и это поведение нам известно
# как переопределение метода(method overriding).
# Полиморфизм позволяет нам иметь доступ к этим переопределённым методам и атрибутам,
# которые имеют то же самое имя, что и в родительском классе.

# Полиморфизм использует одинаковые методы, но с разной реализацией.