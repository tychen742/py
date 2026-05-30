import turtle

wn = turtle.Screen()
tess = turtle.Turtle()


def drawSquare (tt, size):
    for i in range (4):
        tt.forward(size)
        tt.left(90)

tess.penup()
tess.forward(-300)
tess.pendown()

for i in range (10):
    drawSquare(tess,i*9)

    tess.penup()
    tess.forward(i*11)
    tess.pendown()

# drawSquare(tess, i)

wn.exitonclick()

