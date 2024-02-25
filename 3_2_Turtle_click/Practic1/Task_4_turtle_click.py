import turtle

def on_timer():
    print("Прошла 1 секунда")
    # turtle.ontimer(on_timer, 1000)


turtle.ontimer(on_timer, 1000)
turtle.mainloop()

