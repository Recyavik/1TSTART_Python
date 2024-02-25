import random

def createGenerator(a, b, n):
    mylist = range(n)
    for _ in mylist :
        yield random.randint(a, b)

my_generator = createGenerator(10, 15, 5)
for i in my_generator:
    print(i)