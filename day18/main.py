from turtle import Turtle, Screen
import random
timmy = Turtle()

# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)

# #! draw a square
# for _ in range(4):
#     timmy.forward(100)
#     timmy.left(90)

# #! Draw a dashed line
# for _ in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

#! Draw a triangle square pentagon hexagon.....

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)

for shape_side in range(3,11):
    timmy.color(random.choice(colors))
    draw_shape(shape_side)











screen = Screen()
screen.exitonclick()