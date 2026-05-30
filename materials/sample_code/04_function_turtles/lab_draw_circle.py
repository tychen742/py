import turtle
def drawPolygon (t, numSide, sideLength):
    for i in range(numSide):
        t.forward(sideLength)
        t.left(360 / numSide)
# But we talk about circle in radius, not in sides. So, ==> Problem-Solving

def drawCircle (t, r):
    pi = 3.14159
    sideLength = (2*pi*r) / 360
    drawPolygon (t, 360, sideLength)

wn = turtle.Screen()
tess = turtle.Turtle()

# drawPolygon (tess, 360, 2)  # Give number of sides and side length

drawCircle (tess, 50)   # Please give radius to draw a circle

wn.exitonclick()