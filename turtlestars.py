import turtle
from random import randint

window = turtle.Screen()
turtle.bgcolor("black")
turtle.color("yellow")
turtle.title("Turtle Stars")
turtle.speed(0)


def draw_star():
    turns = 6
    turtle.begin_fill()
    while turns > 0:
        turtle.forward(25)
        turtle.left(145)
        turns = turns-1
    turtle.end_fill()


nums_stars = 0
while nums_stars < 100:
    x = randint(-400, 400)
    y = randint(-400, 400)
    draw_star()
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    nums_stars = nums_stars + 1

window.exitonclick()
