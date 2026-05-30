import turtle

def draw (someTurtle, sideLength, numSquare):
    print('something')


    for j in range(numSquare):
        # someTurtle.penup()
        # someTurtle.setposition(-sideLength / 2, -sideLength / 2)
        # someTurtle.pendown()
        for i in range(4):
            someTurtle.forward(sideLength)
            someTurtle.left(90)

        someTurtle.left(360 / numSquare)

        # someTurtle.penup()

def main ():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")
    tess = turtle.Turtle()
    tess.pencolor("blue")
    tess.pensize(2)
    tess.speed(10)
    side_length = 100
    num_square = 20
    draw (tess, side_length, num_square)

    wn.exitonclick()

if __name__ == '__main__':
    main()