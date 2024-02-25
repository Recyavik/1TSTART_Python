import turtle

def polygon(n):
    for _ in range(n):
        t.forward(100)
        t.left(360/n)



sc = turtle.Screen()
sc.setup(600, 600)
t = turtle.Turtle()
while True:
    st = turtle.textinput('Сделайте выбор', 'Что сделать черепахе?')
    print(st)
    if st == 'выход':
        break
    if st == 'шестиугольник':
        polygon(6)
    elif st == 'квадрат':
        polygon(4)
    elif st == 'треугольник':
        polygon(3)


turtle.done()