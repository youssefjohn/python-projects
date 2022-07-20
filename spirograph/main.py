import colorgram
import random
from turtle import Turtle, Screen

color = colorgram.extract('image.jpg', 25)

color_list = []

for color in color:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    color_list.append((r, g, b))

screen = Screen()
screen.colormode(255)
turtle = Turtle()

x = -350
y = -350
turtle.penup()
turtle.hideturtle()
turtle.setpos(x,y)


def coordinates(y):
    global x
    turtle.goto(x, y)


def movement():
    for _ in range(10):
        turtle.dot(20, random.choice(color_list))

        turtle.forward(50)


for _ in range(10):
    y += 50
    movement()
    coordinates(y)


screen.exitonclick()

