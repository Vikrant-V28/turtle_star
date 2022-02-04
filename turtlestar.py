# Python program to draw star Pattern using Turtle Programming

import turtle
from turtle import *

# set the background color of the turtle screen
turtle.Screen().bgcolor("#000")

color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
