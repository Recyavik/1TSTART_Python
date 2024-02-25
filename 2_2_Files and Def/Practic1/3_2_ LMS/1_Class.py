# class НазваниеКласса:
#     атрибуты_класса
#     методы_класса
# Нотация — это соглашение об именовании.

# first_name - under_score (Нотация подчёркивания)
# Person - CamelCase (Верблюжья нотация)

class NameClass:
    pass

instance1 = NameClass()
instance2 = NameClass()

class Person:

    def say(self):
        print("Говорю")

    def go(self):
        print("окей, Иду")

anna = Person()
gleb = Person()

anna.say()
anna.go()
gleb.say()
gleb.go()

class PersonNew:

    def say(self, message):
        print("Говорю: ", message)

    def go(self, speed):
        print("Иду со скоростью: ", speed, "км/ч")

tanya = PersonNew()
nina = PersonNew()
tanya.say("Привет!")
nina.say("Здравствуй!")
tanya.say("Как дела?")
nina.say("Спасибо нормально!")
nina.go(5)


class SuperPerson:

    def say(self, message):
        print("Говорю: ", message)

    def sing(self):
        print("Пою")

    def go(self, speed):
        print("Иду со скоростью: ", speed, "км/ч")
        self.sing()

oleg = SuperPerson()
oleg.say("Привет, я - Олег!")
oleg.go(1)

class Citizen:
    def __init__(self, name):
        self.name = name

    def say(self, message):
        print(self.name, ": говорит - ", message)

    def sing(self):
        print(self.name, ": поёт")

    def go(self, speed):
        print(self.name, "идёт со скоростью: ", speed, "км/ч")
        self.sing()

alex = Citizen("Алексей")
alex.go(4)
alex.say("Что еще вам спеть ?")

sasha = Citizen("Саша")
sasha.name = "Александр"
print(sasha.name)



class PersonFast:
    speed_default = 1

    def __init__(self, name, speed=speed_default):
        self.name = name
        self.speed = speed

    def go(self):
        print(self.name, "идёт со скоростью: ", self.speed, "км/ч")

misha = PersonFast("Миша", 4)
misha.speed = 3
misha.go()

class PersonFast:

    def __init__(self, name="Неизвестное имя", speed=2):
        self.name = name
        self.speed = speed

    def go(self):
        print(self.name, "идёт со скоростью: ", self.speed, "км/ч")

misha = PersonFast("Миша", 4)
misha.speed = 3
misha.go()

