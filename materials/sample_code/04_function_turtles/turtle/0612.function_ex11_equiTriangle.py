import turtle

def drawPoly(someturtle, somesides, somesize):
    # print("Something")
    for i in range (somesides):
        someturtle.forward(somesize)
        someturtle.left(360 / somesides)

def drawEquitriangle(someturtle, somesize):
    drawPoly(someturtle, 3, somesize)

def main():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")

    tess = turtle.Turtle()
    tess.pensize(5)
    tess.color('hotpink')

    # side = 8
    # size = 50

    drawEquitriangle(tess, 100)

    wn.exitonclick()

if __name__ == '__main__':
    main()