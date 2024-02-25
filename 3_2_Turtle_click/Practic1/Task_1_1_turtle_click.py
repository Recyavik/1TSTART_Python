import turtle


# функция для обработки события щелчка левой кнопки мыши
def on_click(x, y):
    turtle.color('blue')
    turtle.goto(x, y)  # перемещение черепашки в точку щелчка
    turtle.color('red')
    turtle.dot(20)  # рисование круга в точке щелчка


# настройка окна
screen = turtle.Screen()
screen.setup(width=500, height=500)
turtle.pensize(3)
screen.title("Обработка события щелчка левой кнопки мыши")
# регистрация обработчика события щелчка левой кнопки мыши
turtle.onscreenclick(on_click, 1)
# запуск цикла обработки событий
turtle.mainloop()

