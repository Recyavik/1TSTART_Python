import turtle
import random as rnd

t = turtle.Turtle()
t.screen.screensize(400, 400, bg="gray")
t.pensize(5)
x = rnd.randint(-200, 200)
y = rnd.randint(-200, 200)
t.penup()
color_list = (["SpringGreen", "DeepSkyBlue", "Aqua", "Maroon", "Show", "Chocolate",
               "Lime", "DarkOrange", "Salmon", "Indigo", "Gold", "Fuchsia"])
color_pen = rnd.choice(color_list)
color_fill = rnd.choice(color_list)
t.goto(x,y)
if color_pen == color_fill:
    color_pen = "black"
    color_fill = "white"
t.pencolor(color_pen)

t.fillcolor("#800000")
t.begin_fill()

t.pendown()
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
