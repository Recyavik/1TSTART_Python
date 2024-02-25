import time
from functools import lru_cache
# Рекурсия — это техника в программировании, при которой функция вызывает
# саму себя напрямую или косвенно. Она может быть очень полезной для решения
# Рекурсия — это техника в программировании, при которой функция вызывает саму себя напрямую или косвенно.
# Она может быть очень полезной для решения определенных задач, но имеет свои ограничения.

# Одно из них — максимальная глубина рекурсии.
#
# В Python предусмотрено ограничение на максимальную глубину рекурсии,
# чтобы предотвратить переполнение стека и последующий сбой программы.
# Это ограничение обычно установлено на достаточно высоком уровне
# (обычно порядка 1000), но иногда, для решения определенных задач,
# может потребоваться увеличить этот лимит.

# Чтобы увеличить максимальную глубину рекурсии, можно использовать
# функцию sys.setrecursionlimit(limit).
# Эта функция устанавливает максимальную глубину рекурсии на указанное значение.
# Но стоит быть осторожным, увеличивая этот лимит, так как это может привести
# к переполнению стека и сбою программы.
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

print(factorial(5))
print(factorial_good(5))
print(factorial_cache(5))
print(factorial_memo(5))


print("Тест 1 Цикл факториал")
start = time.time()
test1 = factorial(600)
print(time.time() - start, "\n")


print("Тест 2 Рекурсия факториал")
start = time.time()
test2 = factorial_good(500)
print(time.time() - start, "\n")

print("Тест 3 Рекурсия факториал с кэш")
start = time.time()
test3 = factorial_cache(500)
print(time.time() - start, "\n")


print("Тест 4 Рекурсия факториал Мемоизация")
start = time.time()
test4 = factorial_memo(500)
print(time.time() - start, "\n")

