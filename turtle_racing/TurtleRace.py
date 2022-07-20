from turtle import Turtle, Screen
import random

colours = ["red", "blue", "yellow", "orange", "green", "purple"]

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bets!", prompt="Which turtle will win the race? Enter a colour: ")
all_turtles = []


x = -230
y = -100
for _ in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours.pop())
    new_turtle.penup()
    new_turtle.goto(x, y=y)
    y += 30
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

print(all_turtles)
while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print(f"You've won! The {winning_colour} turtle is the winner!")
            else:
                print("You lose!")


        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)



screen.exitonclick()




