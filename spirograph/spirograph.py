import random
from turtle import Turtle, Screen
from random import choice

colours = ["red", "blue", "orange", "black", "white", "purple"]


tim = Turtle()
tim.shape("turtle")
tim.color("red")
tim.speed(0)
numbers = 10



for _ in range(200):
    tim.circle(50)
    tim.setheading(numbers)
    numbers += 10


screen = Screen()
screen.exitonclick()

