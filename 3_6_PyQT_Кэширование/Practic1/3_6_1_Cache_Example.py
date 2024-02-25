import time
from functools import lru_cache
import sys
sys.setrecursionlimit(100000)

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
print(test1)
delta_time = time.time_ns() - start_time
print(delta_time, "\n")

print("Тест 2 - Рекурсия с оптимизацией словарём для 490 первых чисел")
start_time = time.time_ns()
test2 = fib_dict(1000)
# print(test2)
delta_time = time.time_ns() - start_time
print(delta_time, "\n")

print("Тест 3 - Рекурсия с внутренней функцией кэширования для 490 первых чисел")
start_time = time.time_ns()
test3 = fib_cache(1490)
# print(test3)
delta_time = time.time_ns() - start_time
print(delta_time, "\n")