import turtle

def drawRectangle(turtle, length, width):
    for i in range (2):
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(width)
        turtle.right(90)

def drawSquare(turtle, side):
    drawRectangle(turtle, side, side)

wn = turtle.Screen()
tess = turtle.Turtle()

# drawRectangle(tess, 20, 250)

drawSquare(tess, 50)

wn.exitonclick()