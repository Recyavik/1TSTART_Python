# T(n) = T(n/3) + T(2n/3) + n

import time
from functools import lru_cache

import sys
sys.setrecursionlimit(10000)

def T(n):
    if n <= 1:
        return 0
    else:
        return T(n/3) + T(2*n/3) + n

@lru_cache()
def T_cache(n):
    if n <= 1:
        return 0
    else:
        return T_cache(n/3) + T(2*n/3) + n

cache_recursive_trees ={}
def T_memo(n):
    if n in cache_recursive_trees:
        return cache_recursive_trees[n]
    if n <= 1:
        return 0
    else:
        result = T_memo(n/3) + T_memo(2*n/3) + n
    cache_recursive_trees[n] = result
    return result



print("Тест 1 Рекурсивное дерево")
start = time.time_ns()
test1 = T(15_000_000)
print(time.time_ns() - start, "\n")


print("Тест 2 Рекурсивное дерево с кэш")
start = time.time_ns()
test2 = T_cache(15_000_000)
print(time.time_ns() - start, "\n")


print("Тест 3 Рекурсивное дерево Мемоизация")
start = time.time_ns()
test3 = T_memo(15_000_000)
print(time.time_ns() - start, "\n")

