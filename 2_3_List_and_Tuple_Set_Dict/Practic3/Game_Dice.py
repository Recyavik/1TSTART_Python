# Два игрока играют в кости, каждый бросает два кубика по очереди 5 раз.
# По правилам игры наблюдатель фиксирует броски первого и второго игрока,
# чтобы подтвердить победу.
# Победа присуждается игроку, который набрал большее количество очков по правилам:
# 6 и 6 - Приз - все очки удваиваются
# 1 и 1 - Штраф - все очки делятся в 2 раза
# Если выпадает только один кубик с 6 - Приз +10 очков
# Если выпадает только один кубик с 1 - Штраф -5 очков
# В конце игры наблюдатель демонстрирует свои записи и объявляет победителя
"""
{1: [6,2], 2:[6,6], 3:[5,1]}
""" #
import random

protocol1 = dict()
protocol2 = dict()
res1 = 0
res2 = 0
for key in range(1, 6):
    print('Бросает 1 игрок, попытка', key)
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    print(a,'и', b)
    s = a + b
    protocol1[key] = list([a, b])
    if s == 12:
        res1 = res1 * 2
    elif s == 2:
        res1 = res1 // 2
    elif a == 6 or b == 6 and s != 12:
        res1 = res1 + 10
    elif a == 1 or b == 1 and s != 2:
        res1 = res1 - 5
    else:
        res1 = res1 + s
    if res1 < 0:
        res1 = 0
    print('Результат 1 игрока', res1)


    print('Бросает 2 игрок, попытка', key)
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    print(a, 'и', b)
    s = a + b
    protocol2[key] = list([a, b])
    if s == 12:
        res2 = res2 * 2
    elif s == 2:
        res2 = res2 // 2
    elif a == 6 or b == 6 and s != 12:
        res2 = res2 + 10
    elif a == 1 or b == 1 and s != 2:
        res2 = res2 - 5
    else:
        res2 = res2 + s
    if res2 < 0:
        res2 = 0
    print('Результат 2 игрока', res2)
    input()

print('Протокол бросков 1 игрока:  ', protocol1)
print('Протокол бросков 2 игрока:  ', protocol2)
print(f"______ ИТОГИ ИГРЫ _________")
print(f"___ {res1} : {res2} ______")
if res1 > res2:
    print('ПОБЕДИЛ 1 игрок!')
elif res2 > res1:
    print('ПОБЕДИЛ 2 игрок!')
else:
    print('Ничья!!')

