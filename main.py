# GC22

import turtle
import random

wn = turtle.Screen()
pirate = turtle.Turtle()

directions = [0, 90, 180, 270]

while True:
    turtle.left(random.choice(directions))
    turtle.forward(100)
wn.mainloop()
