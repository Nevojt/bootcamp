
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter s color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtle = []

pen = Turtle()
pen.hideturtle()
pen.penup()
pen.goto(x=-220, y=170)

#  Created turtle 
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-220, y=y_position[turtle_index])
    all_turtle.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            wining_color = turtle.pencolor()
            if wining_color == user_bet:
                pen.write(f"You've won! The {wining_color} turtle is the winner!", font=("Arial", 16, "normal"))
            else:
                pen.write(f"You've lost! The {wining_color} turtle is the winner!", font=("Arial", 16, "normal"))

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)






screen.exitonclick()