from turtle import Turtle, Screen

timmy = Turtle()

# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)

#! draw a square
for _ in range(4):
    timmy.forward(100)
    timmy.left(90)

#! Draw a dashed line
for _ in range(15):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()

















screen = Screen()
screen.exitonclick()