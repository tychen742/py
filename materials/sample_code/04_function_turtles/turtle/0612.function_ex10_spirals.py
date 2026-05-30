import turtle
import tkinter

def drawSpiral (someTurtle, length, numLoop, turnDegree):
    # print ("something")
    for i in range (numLoop):
        someTurtle.forward(length)
        someTurtle.left(turnDegree)
        # someTurtle.forward(length = length + length)
        length = length + 2

def main ():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")
    tess = turtle.Turtle()
    tess.color("blue")
    tess.pensize(2)
    tess.speed(10)
    tess.shape("turtle")
    initial_length = 2
    num_loop = 75
    # turn_degree = 91

    tess.penup()
    tess.setposition(-100, 0)
    tess.pendown()
    drawSpiral(tess, initial_length, num_loop, 90)

    tess.penup()
    tess.setposition(100, 0)
    tess.pendown()
    drawSpiral(tess, initial_length, num_loop, 91)

    wn.exitonclick()
    # tkinter.mainloop()


if __name__ == '__main__':
    main()

