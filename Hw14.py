import turtle
turtle.Screen().bgcolor("Light blue")
turtle.Screen().setup(300,400)
square=turtle.Turtle()
num_of_sides=4
side_length=75 
angle=360.0/num_of_sides
for i in range(num_of_sides):
    square.forward(side_length)
    square.right(angle)