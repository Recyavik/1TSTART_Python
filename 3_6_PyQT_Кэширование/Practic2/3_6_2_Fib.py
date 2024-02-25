import time
from functools import lru_cache
from sys import getrecursionlimit
from sys import setrecursionlimit
setrecursionlimit(10000)

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

cache = {}
def fib_dict(n):
    if n in cache:
        return cache[n]
    result = 0
    if n <= 1:
        result = n
    else:
        result = fib_dict(n-1) + fib_dict(n-2)
    cache[n] = result
    return result

@lru_cache
def fib_cache(n):
    if n <= 1:
        return n
    else:
        return fib_cache(n-1) + fib_cache(n-2)


print("Тест 1 - Обычная рекурсия чисел Фибоначчи для 35 первых чисел")
start_time = time.time_ns()
test1 = fib(35)
delta_time = time.time_ns() - start_time
print('{0:,}  н.секунд'.format(delta_time).replace(',', ' '), '\n')

print("Тест 2 - Рекурсия с оптимизацией словарём для 4900 первых чисел")
start_time = time.time_ns()
test2 = fib_dict(4900)
delta_time = time.time_ns() - start_time
print('{0:,}  н.секунд'.format(delta_time).replace(',', ' '), '\n')

print("Тест 3 - Рекурсия с внутренней функцией кэширования для 490 первых чисел")
start_time = time.time_ns()
test3 = fib_cache(490)
delta_time = time.time_ns() - start_time
print('{0:,}  н.секунд'.format(delta_time).replace(',', ' '), '\n')