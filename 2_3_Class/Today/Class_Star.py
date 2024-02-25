import turtle


t = turtle.Turtle()
t.speed(0)
for i in range(5):
    t.right(180-180/5)
    t.fd(200)
t.penup()
t.goto(200, 200)
t.pendown()


turtle.done()