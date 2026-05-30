import turtle

def drawSquare (turt, sideLength, moveDist, numBox):
#     # draw a square
    for j in range (numBox):
        for i in range (4):
            turt.forward(sideLength)
            turt.left(90)

#     # move ahead
        turt.penup()
        turt.forward(sideLength + moveDist)
        turt.pendown()

def main ():
    print("something") # test

    # define turtle
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")    # define screen color
    tess = turtle.Turtle()
    tess.pensize(5)# define line width
    tess.color("hotpink")
    tess.speed(2)

    # define arguments: sideLength, moveDist, numBox
    side_length = 40
    move_dist = 30
    num_box = 5

    # call function drawSquare()
    drawSquare(tess, side_length, move_dist, num_box)

    wn.exitonclick()

if __name__ == '__main__':
    main()