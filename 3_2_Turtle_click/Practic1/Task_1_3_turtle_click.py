import turtle

def on_drag(x, y):
    turtle.ondrag(None)  # Отключаем текущий обработчик, чтобы избежать рекурсии
    turtle.goto(x, y)
    turtle.ondrag(on_drag)  # Повторно включаем обработчик

turtle.shape("circle")
turtle.color("red")
turtle.penup()
turtle.ondrag(on_drag)

turtle.mainloop()
