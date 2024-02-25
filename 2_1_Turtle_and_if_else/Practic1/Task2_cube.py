import turtle

t = turtle.Turtle()
t.speed(0)
t.pensize(3)
t.color("red")
t.penup()
t.goto(50, 50)
t.pendown()
t.left(90)

t.right(45)
t.forward(100)
t.right(45)
t.forward(200)
t.right(135)
t.forward(100)
t.right(45)
t.forward(200)

t.penup()
t.right(90)
t.forward(200)
t.pendown()

t.right(45)
t.forward(100)
t.right(45)
t.forward(200)

t.right(135)
t.forward(100)
t.right(45)
t.forward(200)

t.right(90)
t.backward(200)

t.penup()
t.right(45)
t.forward(100)
t.pendown()
t.left(45)
t.color("lime")
t.forward(200)

t.penup()
t.right(90)
t.color("red")
t.forward(200)
t.pendown()
t.right(90)

t.forward(200)

t.penup()
t.right(45)
t.forward(100)
t.pendown()
t.right(135)
t.forward(200)

t.penup()
t.goto(0,0)


turtle.done()