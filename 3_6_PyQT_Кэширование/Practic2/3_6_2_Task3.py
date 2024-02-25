# Если применение рекурсии при решении задачи неизбежно,
# есть простой способ ускорить выполнение функции – для этого используют
# декоратор @lru_cache() модуля functools.
# Сравним скорость выполнения рекурсивного кода при решении следующей олимпиадной задачи.

# Гармони́ческий ряд – сумма, составленная из бесконечного количества членов,
# обратных последовательным числам натурального ряда
# Ряд назван гармоническим, так как складывается из «гармоник»:
# n-я гармоника, извлекаемая из скрипичной струны, – это основной тон,
# производимый струной длиной 1/n от длины исходной струны.



import time
from sys import setrecursionlimit
setrecursionlimit(30000)

# Решение 1 – итеративное:
def harmonic_iter(n):
    res = 1.0
    for i in range(2, n+1):
        res += 1 / i
    return res

start_time = time.time_ns()
print(harmonic_iter(25000))
time_run = time.time_ns() - start_time
print('Время выполнения без кэширования итеративно', end=' ')
print('{0:,}  н.секунд'.format(time_run).replace(',', ' '))

def harmonic_rec(n):
   if n == 1: # граничный случай
       return 1
   else: # рекурсивный случай
       return 1 / n + harmonic_rec(n - 1)

start_time = time.time_ns()
print(harmonic_rec(25000))
time_run = time.time_ns() - start_time
print('Время выполнения без кэширования рекурсивно ', end=' '' ')
print('{0:,}  н.секунд'.format(time_run).replace(',', ' '))
import functools
@functools.lru_cache(maxsize=None)

def harmonic_rec_cache(n):
   if n == 1: # граничный случай
       return 1
   else: # рекурсивный случай
       return 1 / n + harmonic_rec(n - 1)

start_time = time.time_ns()
print(harmonic_rec_cache(25000))
time_run = time.time_ns() - start_time
print('Время выполнения c кэшированием рекурсивно ', end=' ')
print('{0:,}  н.секунд'.format(time_run).replace(',', ' '))

# Решение 4 – со словарём:
cache = {}
def harmonic_dict(n):
    if n in cache:
        return cache[n]
    if n <= 1:
        return 0
    res = 0
    if n == 1:  # граничный случай
        return 1
    else:
        res = 1 / n + harmonic_rec(n - 1)
    cache[n] = res
    return res

start_time = time.time_ns()
print(harmonic_dict(25000))
time_run = time.time_ns() - start_time
print(f'Время выполнения c кэшированием и словарём ', end=' ')
print('{0:,}  н.секунд'.format(time_run).replace(',', ' '))

# Рекурсию с кэшированием стоит применять для решения задач, в которых:
#
# Используется древовидная структура данных.
# Нужно предусмотреть возврат к предыдущей отправной точке (например, при поиске выхода из лабиринта).
# Глубина рекурсивных вызовов находится в пределах разумного и не приведет к переполнению стека.
# Во всех остальных случаях целесообразнее использовать итерацию либо итерацию и стек.