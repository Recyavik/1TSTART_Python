from sys import setrecursionlimit
import time
setrecursionlimit(30000)
cache = {}
def harmonic_dict(n):
    if n in cache:
        return cache[n]
    if n <= 1:
        return 0
    res = 0
    if n == 1:
        return 1
    else:
        res = 1/n + harmonic_dict(n-1)
    cache[n] = res
    return res


def harmonic_iter(n):
    res = 1.0
    for i in range(2, n+1):
        res += 1/i
    return res

def harmonic_rec(n):
    if n == 1:
        return 1
    else:
        return 1 / n + harmonic_rec(n-1)

import functools
@functools.lru_cache
def harmonic_rec_cache(n):
    if n == 1:
        return 1
    else:
        return 1 / n + harmonic_rec_cache(n-1)


start_time = time.time_ns()
print(harmonic_iter(25000))
delta_time = time.time_ns() - start_time
print("Тест 1 - Время выполнения без кэширования итеративно", end=' ')
print("{0:,} н.секунд".format(delta_time).replace(",",' '))

print(harmonic_rec(25000))
delta_time = time.time_ns() - start_time
print("Тест 2 - Время выполнения без кэширования рекурсивно", end=' ')
print("{0:,} н.секунд".format(delta_time).replace(",",' '))


print(harmonic_rec_cache(490))
delta_time = time.time_ns() - start_time
print("Тест 3 - Время выполнения с встроенным кэшированием рекурсивно", end=' ')
print("{0:,} н.секунд".format(delta_time).replace(",",' '))

print(harmonic_dict(25000))
delta_time = time.time_ns() - start_time
print("Тест 4 - Время выполнения с кэшированием через словарь рекурсивно", end=' ')
print("{0:,} н.секунд".format(delta_time).replace(",",' '))