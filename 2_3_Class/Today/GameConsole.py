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


class Hero:
    def __init__(self, name='Герой'):
        self.name = name
        self.hp = 100
        self.damage = 10
        self.color = f'\033[93m'

    def attack(self, obj):
        if rnd.randint(1, 10) == 1:
            critical_damage = rnd.randint(20, 100)
            self.damage = critical_damage
        print(self.color, end='')
        print(self.name, 'атакует!', obj.name, 'силой', self.damage, end='')
        obj.hp = obj.hp - self.damage
        print(f'\033[00m')

    def info(self):
        print('Жизнь', self.name, '=', self.hp)


class Enemy:
    def __init__(self, name='Враг'):
        self.name = name
        self.hp = 200
        self.damage = 15
        self.color = f'\033[91m'

    def attack(self, obj):
        if rnd.randint(1, 10) == 1:
            critical_damage = rnd.randint(10, 100)
            self.damage = critical_damage
        print(self.color, end='')
        print(self.name, 'атакует!', obj.name, 'силой', self.damage, end='')
        obj.hp = obj.hp - self.damage
        print(f'\033[00m')

    def info(self):
        print('Жизнь', self.name, '=', self.hp)


class Doc:
    def __init__(self, name='Лекарь'):
        self.name = name
        self.hp = 100
        self.damage = 5
        self.heal = 10
        self.color = '\033[94m'

    def attack(self, obj):
        print(self.color, end='')
        print(self.name, 'атакует!', obj.name, 'силой', self.damage, end='')
        obj.hp = obj.hp - self.damage
        print(f'\033[00m')

    def healing(self, obj):
        print(self.color, end='')
        print(self.name, 'лечит!', obj.name, 'силой', self.heal, end='')
        obj.hp = obj.hp + self.heal
        print(f'\033[00m')

    def info(self):
        print('Жизнь', self.name, '=', self.hp)


def battle(hero, enemy, doctor):
    while hero.hp != 0 or enemy.hp != 0 or doctor.hp != 0:
        if enemy.hp <=0 and (hero.hp <=0 or doctor.hp <=0):
            print('Ничья!')
            break
        elif hero.hp <= 0:
            print(hero.name,  'Погиб!')
            print('Победил - ', enemy.name)
            break
        elif enemy.hp <= 0:
            print(enemy.name,  'Погиб!')
            print('Победили - ', hero.name, 'и', doctor.name)
            break
        elif doctor.hp <= 0:
            print(doctor.name,  'Погиб!')
            print('Победил - ', enemy.name)
            break


        if rnd.randint(1, 10) % 2 == 0:
            enemy.attack(hero)
        else:
            enemy.attack(doctor)
        hero.info()
        doctor.info()



        hero.attack(enemy)
        enemy.info()


        if rnd.randint(1, 10) % 2 == 0:
            doctor.attack(enemy)
            enemy.info()
        else:
            doctor.healing(hero)
            hero.info()


hero1 = Hero('Буратино')
enemy1 = Enemy('Карабас-Барабас')
doc1 = Doc('Мальвина')

battle(hero1, enemy1, doc1)
