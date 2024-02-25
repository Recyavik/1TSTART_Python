class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def make_sound(cls):
        print("Животное издаёт звук: ")

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
cat3 = Cat("Коша", 5)


dog1 = Dog("Шарик", 7)
dog2 = Dog("Рекс", 12)
dog3 = Dog("Ирма", 3)

list_animal = [cat1, cat2, cat3, dog1, dog1, dog2, dog3]
for el in list_animal:
    el.make_sound()

