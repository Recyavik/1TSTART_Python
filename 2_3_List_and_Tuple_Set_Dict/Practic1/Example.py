a = [1, 2, 3, 4, 5]
b = a
print(a, id(a))
print(b, id(b))
a.append(6)
print(a)
print(b)

c = a.copy()
a.append(7)
print(a, id(a))
print(c, id(c))
