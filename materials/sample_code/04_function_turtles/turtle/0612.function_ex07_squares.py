import turtle

def drawSquare (turt, sideLength, numBox):
#     # draw a square
    for j in range (numBox):
        turt.penup()
        turt.setposition(-sideLength/2, -sideLength/2)

        turt.pendown()
        for i in range (4):
            turt.forward(sideLength)
            turt.left(90)
        turt.penup()

        sideLength = sideLength + 20


#     # move ahead

        # turt.forward(sideLength + 20)


def main ():
    # print("something") # test
    # define turtle
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")    # define screen color
    tess = turtle.Turtle()
    tess.pensize(5)# define line width
    tess.color("hotpink")
    tess.speed(2)

    # define arguments: sideLength, moveDist, numBox
    side_length = 20
    # move_dist = side_length + 20
    num_box = 5

    # call function drawSquare()
    drawSquare(tess, side_length, num_box)

    wn.exitonclick()

if __name__ == '__main__':
    main()