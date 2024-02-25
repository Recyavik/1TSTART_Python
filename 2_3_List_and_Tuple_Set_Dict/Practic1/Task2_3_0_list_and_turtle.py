
import turtle


colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']

t = turtle.Turtle()
t.speed(0)
t.width(5)
for i in range(120):
    t.pencolor(colors[i % 6])
    t.forward(3 * i)
    t.right(60)

turtle.done()

