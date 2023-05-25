from turtle import Turtle, Screen, colormode
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

# #! Draw a triangle square pentagon hexagon.....

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# def draw_shape(num_sides):
#     angle = 360/num_sides
#     for _ in range(num_sides):
#         timmy.forward(100)
#         timmy.right(angle)

# for shape_side in range(3,11):
#     timmy.color(random.choice(colors))
#     draw_shape(shape_side)


# #! Draw a random walk

colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

# directions =[0,90,180,270]
# timmy.pensize(10)
# timmy.speed("fastest")

# for _ in range(200):
#     timmy.color(random_color())
#     #timmy.color(random.choice(colors))
#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))


#! Draw a spirograph
timmy.speed(0)

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading()+size_of_gap)


draw_spirograph(7)
























screen = Screen()
screen.exitonclick()