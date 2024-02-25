import turtle

t = turtle.Turtle()
t.begin_fill()
t.fillcolor('red')
t.circle(50)
t.end_fill()
t.forward(60)
t.right(90)
t.left(90)
t.penup()
t.left(90)
t.backward(30)
t.write(" Hello, World!", font=("Arial", 16, "normal"))
t.pendown()
t.pensize(3)
t.pensize(5)
# Изменение цвета пера на красный
t.pencolor("red")
# Начало закраски фигуры с зеленым цветом
t.begin_fill()
t.fillcolor("green")
# Нарисовать квадрат
t.forward(200)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
# Закончить закраску
t.end_fill()
t.pencolor('green')


turtle.done()