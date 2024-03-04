from random import shuffle
from turtle import Screen, Turtle

def shape(length, sides, angle):
    """draws one shape based on the length, sides and angle arguments passed to it
    """
    for i in range(sides):
        sam.fd(length)
        sam.rt(angle)

# main
sam = Turtle()
screen = Screen()
colours = ["red", "orange", "yellow", "green", "blue", "purple"]

sam.pensize(5)
sam.pendown()
screen.bgcolor("black")

# create a pattern using octagons
for i in range(16):
    shuffle(colours)
    sam.pencolor(colours[0])
    shape(50, 8, 45)
    sam.rt(22.5)

screen.exitonclick()
