import keyword
import turtle

wn = turtle.Screen()
wn.title("Графический редактор")
wn.setup(800, 600)
wn.getcanvas().config(cursor="arrow")
wn.tracer(0)

pensize = 1
pen = turtle.Turtle()
pen.pencolor('black')
pen.penup()
flag = False
pen.shapesize(pensize / 3)
pen.hideturtle()
print("log: Перо поднято")

def exit_bye():
    wn.bye()

def change_color_red():
    pen.pencolor('red')
    print("log: Установлен цвет пера красный")

def change_color_green():
    pen.pencolor('green')
    print("log: Установлен цвет пера зеленый")

def change_color_blue():
    pen.pencolor('blue')
    print("log: Установлен цвет пера синий")

def pen_up_down(x, y):
    global flag
    if flag:
        pen.penup()
        pen.hideturtle()
        print("log: Перо поднято")
    else:
        pen.showturtle()
        pen.goto(x, y)
        pen.pendown()
        print("log: Перо опущено")
    flag = not flag

def draw_line(x, y):
    print(f"log: Перо в координатах: ({x}, {y})")
    pen.goto(x, y)

def change_size_pen_inc():
    global pensize
    if pensize < 10:
        pensize += 1
    pen.pensize(pensize)
    pen.shapesize(pensize/3)
    print("log: Увеличили толщину пера")

def change_size_pen_dec():
    global pensize
    pensize -= 1
    pen.pensize(pensize)
    pen.shapesize(pensize/3)
    print("log: Уменьшили толщину пера")

while True:
    wn.update()
    wn.listen()
    wn.onscreenclick(draw_line, btn=1)
    wn.onscreenclick(pen_up_down, btn=3)

    wn.onkey(change_size_pen_inc, 'Up')
    wn.onkey(change_size_pen_dec, 'Down')

    wn.onkey(change_color_red, 'r')
    wn.onkey(change_color_red, 'R')

    wn.onkey(change_color_green, 'g')
    wn.onkey(change_color_green, 'G')

    wn.onkey(change_color_blue, 'b')
    wn.onkey(change_color_blue, 'B')



