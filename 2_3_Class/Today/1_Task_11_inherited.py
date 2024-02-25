class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def make_sound(cls):
        print("Животное издаёт звук: ", end='')


class Cat(Animal):
    def make_sound(self):
        super().make_sound()
        print("Мяу")


class Dog(Animal):
    def make_sound(self):
        super().make_sound()
        print("Гав")


cat = Cat("Мурзик", 3)
cat.make_sound()  # Выведет "Мяу"
dog = Dog("Шарик", 5)
dog.make_sound()  # Выведет "Гав"
