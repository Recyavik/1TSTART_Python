import random as rnd


class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def attack(self, target):
        damage = rnd.randint(1, 10)
        print(f"{self.name} атакует {target.name} и наносит урон {damage} единиц")
        target.hp -= damage

    def show_hp(self):
        print(f"{self.name} имеет {self.hp} здоровья")


class Player(Character):
    def __init__(self, name):
        super().__init__(name, hp=100)

    def heal(self):
        heal_amount = rnd.randint(1, 10)
        print(f"{self.name} восстанавливает {heal_amount} здоровья")
        self.hp += heal_amount


class Enemy(Character):
    def __init__(self, name):
        super().__init__(name, 50)

    def ai(self, players):
        target = rnd.choice(players)
        self.attack(target)


def main():
    player1 = Player("Игрок 1")
    player2 = Player("Игрок 2")
    enemy1 = Enemy("Враг 1")
    enemy2 = Enemy("Враг 2")
    players = [player1, player2]
    enemies = [enemy1, enemy2]
    while True:
        for player in players:
            player.show_hp()
        for enemy in enemies:
            enemy.show_hp()

        for player in players:
            command = input(f"{player.name} выбирает действие а - атака, х - аптечка: ")
            if command == 'а' or command == 'a':
                target = rnd.choice(enemies)
                player.attack(target)
            elif command == 'х' or command == 'x':
                player.heal()
        for enemy in enemies:
            enemy.ai(players)

        if all(player.hp <= 0 for player in players):
            print("Поражение!")
            break
        if all(enemy.hp <= 0 for enemy in enemies):
            print("Победа")
            break


main()
