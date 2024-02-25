import turtle
import random
wn = turtle.Screen()
wn.title("Фантастическая Квест-игра")
wn.bgcolor("white")
wn.setup(width=800,height=600)
knight = turtle.Turtle()
knight.shape("square")
knight.color("blue")
knight.penup()
knight.goto(-100,0)
mage = turtle.Turtle()
mage.shape("circle")
mage.color("red")
mage.penup()
mage.goto(100,0)
elf = turtle.Turtle()
elf.shape("square")
elf.color("green")
elf.penup()
elf.goto(0,0)

def move_up(character):
    y = character.ycor()
    character.sety(y + 20)

def left(character):
    x = character.xcor()
    character.setx(x - 20)

def right(character):
    x = character.xcor()
    character.setx(x + 20)

def move_down(character):
    y = character.ycor()
    character.sety(y-20)

wn.listen()
wn.onkeypress(lambda:move_up(knight),"w")
wn.onkeypress(lambda:move_down(knight),"s")
wn.onkeypress(lambda:right(knight),"d")
wn.onkeypress(lambda:left(knight),"a")

wn.onkeypress(lambda:move_up(mage),"i")
wn.onkeypress(lambda:move_down(mage),"k")

wn.onkeypress(lambda:move_up(elf),"Up")
wn.onkeypress(lambda:move_down(elf),"Down")

wn.mainloop()