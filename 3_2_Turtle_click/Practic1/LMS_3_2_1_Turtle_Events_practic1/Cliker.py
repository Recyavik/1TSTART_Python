import turtle
import random


def move_button():
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    button.goto(x, y)


def button_clicked(x, y):
    move_button()
    update_score()


def update_score():
    global score
    score += 1
    score_pen.clear()
    score_pen.write("Score: {}".format(score), align="center", font=("Arial", 24, "bold"))


score = 0
screen = turtle.Screen()
screen.title("Clicker")
screen.bgcolor("white")

button = turtle.Turtle()
button.speed(0)
button.shape("circle")
button.color("red")
button.penup()
move_button()

score_pen = turtle.Turtle()
score_pen.hideturtle()
score_pen.speed(0)
score_pen.color("black")
score_pen.penup()
score_pen.goto(0, 260)
score_pen.write("Score: {}".format(score), align="center", font=("Arial", 24, "bold"))

score = 0
button.onclick(button_clicked)
turtle.mainloop()
