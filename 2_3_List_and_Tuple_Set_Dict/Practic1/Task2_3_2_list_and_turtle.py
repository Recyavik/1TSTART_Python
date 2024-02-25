import turtle

w = turtle.screensize(500, 500, bg='black')
colors = ["red", "blue", "green", "yellow", "purple", "orange"]
turtle.speed(0)
turtle.pensize(5)

for x in range(360):
    turtle.pencolor(colors[x % 6])
    turtle.width(int(x / 100 + 1))
    turtle.forward(x)
    turtle.left(59)

turtle.done()


