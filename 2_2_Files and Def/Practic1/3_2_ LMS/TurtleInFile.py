from tkinter import *
import turtle as t

count = 1
while count <= 5:
    t.forward(300)
    t.right(144)
    count += 1

ts = t.getscreen()
ts.getcanvas().postscript(file='picture.eps')


