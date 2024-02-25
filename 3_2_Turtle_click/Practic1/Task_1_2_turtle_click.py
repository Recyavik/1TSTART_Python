import turtle

score = 0

def on_click(x, y):
    global score
    score += 1
    print(f"Клик! Очки: {score}")

turtle.onscreenclick(on_click)
turtle.mainloop()
