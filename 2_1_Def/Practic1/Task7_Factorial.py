def factorial(n):
    if n > 1 and isinstance(n, int):
        f = 1
        for x in range(1, n + 1):
            f = f * x
        return f
    else:
        pass

print(factorial(50))
# 50! = 1 * 2 * 3 * ... * 49 * 50