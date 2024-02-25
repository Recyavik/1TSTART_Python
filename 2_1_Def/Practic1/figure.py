import math

def rectangle(a, b):
    p = (a + b) * 2
    s = a * b
    return p, s


def s_circle(radius):
    s = math.pi * radius ** 2
    return s

def area_triangle(a, b, c):
    if a + b > c and b + c > a and a + c > b:
        p = (a + b + c) / 2
        s = (p * (p-a) * (p-b) * (p-c)) ** 0.5
    else:
        s = None
        p = None
    return s, p


