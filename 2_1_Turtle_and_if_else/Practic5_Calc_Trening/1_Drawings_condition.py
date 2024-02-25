import turtle
import random as rnd


t = turtle.Turtle()
t.screen.screensize(400, 400, bg="gray")
turtle.title("Мои рисунки с условием")
t.pensize(5)

x = rnd.randint(-200, 200)
y = rnd.randint(-200, 200)
t.penup()
t.goto(x, y)
t.pendown()
color_list = (["SpringGreen", "DeepSkyBlue", "Aqua", "Maroon", "Snow", "Chocolate", "lime", "DarkOrange", "Salmon",
               "Fuchsia", "Indigo", "Gold"])
color_pen = rnd.choice(color_list)
color_fill = rnd.choice(color_list)
if color_pen == color_fill:
    color_pen = "black"
    color_fill = "white"
t.pencolor(color_pen)
t.fillcolor(color_fill)

t.begin_fill()
side = rnd.randint(30, 200)
if 30 <= side < 60 or 120 <= side < 200:
    t.forward(side)
    t.right(120)
    t.forward(side)
    t.right(120)
    t.forward(side)
    t.right(120)
else:
    t.forward(side)
    t.right(90)
    t.forward(side)
    t.right(90)
    t.forward(side)
    t.right(90)
    t.forward(side)
    t.right(90)

t.end_fill()
t.screen.onscreenclick(t.goto)
t.screen.mainloop()
turtle.done()
