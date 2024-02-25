"""
Составить консольную игру битвы бот-персонажей: Враг, Герой и Лекарь без участия пользователя
Битва:
Враг наносит только урон или случайный критический урон с вероятностью в 10% Герою или Лекарю
Герой наносит только урон или случайный критический урон с вероятностью в 10%
Лекарь может наносить слабый урон Врагу или лечить Героя с вероятностью 50/50
Игра заканчивается, если один из персонажей погибает (Побеждает Враг или Герой с Лекарем)
В любой момент можно запросить уровень здоровья у любого персонажа
hp - уровень жизни, damage - урон (сила повреждения), heal - аптечка (сила лечения)
""" #
import random as rnd
import time
class Character:
    name = 'Персонаж'
    hp = 100
    damage = 10
    color = f'\033[00m'

    def info(self):
        print('Жизнь', self.name, '=', self.hp)

    def attack(self, obj):
        print(self.color, end='')
        print(self.name, 'атакует', obj.name, 'силой', self.damage, end='')
        obj.hp = obj.hp - self.damage
        print(f'\033[00m')

class Hero(Character):
    def __init__(self, name='Герой'):
        self.name = name
        self.color = f'\033[93m'

    def attack(self, obj):
        if rnd.randint(1, 10) == 1:
            critical_damage = rnd.randint(20, 100)
            self.damage = critical_damage
        super().attack(self)

class Enemy(Character):
    def __init__(self, name='Враг'):
        self.name = name
        self.hp = 200
        self.damage = 15
        self.color = f'\033[91m'

    def attack(self, obj):
        if rnd.randint(1, 10) == 1:
            critical_damage = rnd.randint(20, 100)
            self.damage = critical_damage
        super().attack(self)

class Doc(Character):

    def __init__(self, name='Лекарь'):
        self.name = name
        self.damage = 5
        self.color = f'\033[94m'
        self.heal = 10

    def healing(self, obj):
        print(self.color, end='')
        print(self.name, 'лечит', obj.name, 'силой', self.heal, end='')
        obj.hp = obj.hp + self.heal
        print(f'\033[00m')

def battle(hero, enemy, doctor):
    while hero.hp !=0 or enemy.hp !=0 or doctor.hp != 0:
        if hero.hp <= 0:
            print(hero.name, 'Погиб!')
            print('Победил - ', enemy.name)
            break
        if enemy.hp <= 0:
            print(enemy.name, 'Погиб!')
            print('Победили: ', hero.name, 'и', doctor.name)
            break
        if doctor.hp <= 0:
            print(doctor.name, 'Погиб!')
            print('Победил - ', enemy.name)
            break

        if rnd.randint(1, 10) % 2 == 0:
            enemy.attack(hero)
        else:
            enemy.attack(doctor)
        hero.info()
        doctor.info()
        time.sleep(1)

        hero.attack(enemy)
        enemy.info()
        time.sleep(1)

        if rnd.randint(1, 3)  == 1:
            doctor.attack(enemy)
        elif rnd.randint(1, 3)  == 2:
            doctor.healing(hero)
        else:
            doctor.healing(doctor)

        time.sleep(1)





d = Doc('Мальвина')
e = Enemy('Карабас Барабас')
h = Hero('Буратино')

battle(hero=h, enemy=e, doctor=d)


