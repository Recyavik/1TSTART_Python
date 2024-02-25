import time
from functools import lru_cache

import sys
sys.setrecursionlimit(3000)

def factorial(n):
    p = 1
    for i in range(1, n + 1):
        p = p * i
    return p

def factorial_good(n):
    if n <= 1:
        return 1
    else:
        return factorial_good(n - 1) * n

@lru_cache()
def factorial_cache(n):
    if n <= 1:
        return 1
    else:
        return factorial_cache(n-1) * n

cache_factorial ={}
def factorial_memo(n):
    if n in cache_factorial:
        return cache_factorial[n]
    if n <= 1:
        return 1
    else:
        result = factorial_memo(n - 1) * n
    cache_factorial[n] = result
    return result


print("Тест 1 Итерация факториал")
start = time.time_ns()
test1 = factorial(1500)
print(time.time_ns() - start, "\n")

print("Тест 2 Рекурсия факториал")
start = time.time_ns()
test2 = factorial_good(1500)
print(time.time_ns() - start, "\n")

print("Тест 3 Рекурсия факториал с кэш")
start = time.time_ns()
test3 = factorial_cache(490)
print(time.time_ns() - start, "\n")

print("Тест 4 Рекурсия факториал Мемоизация")
start = time.time_ns()
test4 = factorial_memo(1500)
print(time.time_ns() - start, "\n")

