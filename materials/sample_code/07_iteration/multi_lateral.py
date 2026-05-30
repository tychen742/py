import turtle
wn = turtle.Screen()
tess = turtle.Turtle()

side = int(input("What is the number of sides? "))
length = int(input ("What is the length of the side? "))
color_turtle = input ("What is the color of the turtle? ")
color_fill = input ("What is the fill color? ")

tess.color(color_turtle)
tess.fillcolor(color_fill)

tess.begin_fill()
for i in range (side):
    tess.forward(length)
    tess.left(360/side)
tess.end_fill()
#tess.fillcolor(color)
# test
wn.exitonclick()