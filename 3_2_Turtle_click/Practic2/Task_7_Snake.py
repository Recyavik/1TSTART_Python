import turtle
import time
import random


delay = 0.1
score = 0
high_score = 0

# Создаём окно для змейки
wn = turtle.Screen()
wn.title("Игра змейка")
wn.bgcolor("green")
# ширина и высота могут быть установлены по выбору пользователя
wn.setup(width=600, height=600)
wn.tracer(0)

# Голова змейки
head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# еда в игре
food = turtle.Turtle()
colors = random.choice(['red', 'yellow', 'black'])
shapes = random.choice(['square', 'triangle', 'circle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 100)

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Набрано очков : 0  Рекорд : 0 ", align="center",
          font=("candara", 24, "bold"))


# назначение ключевых направлений
def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

segments = []

# Основной игровой процесс
while True:
    wn.update()
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"
        colors = random.choice(['red', 'blue', 'pink'])
        shapes = random.choice(['square', 'circle'])
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Набрано очков : {}  Рекорд : {} ".format(
            score, high_score), align="center", font=("candara", 24, "bold"))

    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)

        # Добавление сегмента
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("orange")  # tail colour
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.001
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Набрано очков : {}  Рекорд : {} ".format(
            score, high_score), align="center", font=("candara", 24, "bold"))
    # Проверка столкновений головы с сегментами тела
    for index in range(len(segments) - 1, 0, -1):
        x = int(segments[index - 1].xcor())
        y = int(segments[index - 1].ycor())
        segments[index].goto(x, y)
    if len(segments) > 0:
        x = int(head.xcor())
        y = int(head.ycor())
        segments[0].goto(x, y)

    move()

    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            for segment in segments:
                segment.goto(0,0)
            segments.clear()


    time.sleep(delay)



wn.mainloop()