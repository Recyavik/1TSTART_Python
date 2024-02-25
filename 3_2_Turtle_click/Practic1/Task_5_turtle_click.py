import turtle

def on_resize(event):
    turtle.write("Window resized!", align="center", font=("Arial", 16, "normal"))
    print('Произошло изменение размера окна')

turtle.Screen().screensize(400, 400)
turtle.getcanvas().bind("<Configure>", on_resize)
turtle.Screen().listen()
turtle.mainloop()

