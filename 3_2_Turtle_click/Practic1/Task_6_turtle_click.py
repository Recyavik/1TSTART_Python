import turtle


# функция, которая рисует квадрат
def draw_square(x, y):
    turtle.setpos(x, y)
    turtle.begin_fill()
    turtle.pencolor("black")
    turtle.pensize(3)
    turtle.pendown()
    for i in range(4):
        turtle.forward(50)
        turtle.left(90)
    turtle.penup()


# функция, которая закрашивает
def paint_square(x, y):
    turtle.setpos(x, y)
    turtle.fillcolor("red")
    turtle.end_fill()


turtle.penup()
# регистрация обработчика события нажатия ЛКМ
turtle.onscreenclick(draw_square, btn=1, add=None)
turtle.listen()
# регистрация обработчика события ПКМ
turtle.onscreenclick(paint_square, btn=3, add=None)
# запуск цикла обработки событий
turtle.mainloop()