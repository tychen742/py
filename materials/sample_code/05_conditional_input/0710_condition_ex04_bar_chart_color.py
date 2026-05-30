import turtle

def drawBar(turtle, bar_list):
    # for i in range (bar_list):
    for i in bar_list:
        if (i >= 200):
            turtle.fillcolor("red")
        elif (200 > i >= 100):
            turtle.fillcolor(("yellow"))
        else:
            turtle.fillcolor("green")

        turtle.begin_fill()
        turtle.left(90)
        turtle.forward(i)
        turtle.write(str(i))  # write the value
        turtle.right(90)
        turtle.forward(40)
        turtle.right(90)
        turtle.forward(i)
        turtle.left(90)
        turtle.end_fill()

def main ():
    wn = turtle.Screen()    # create turtle/screen here
    border = 10
    # maxheight = max(xs)
    # numbars = len(xs)
    # wn.setworldcoordinates(0 - border, 0 - border, 40 * numbars + border, maxheight + border)

    tess = turtle.Turtle()
    tess.pensize(3)
    tess.color("blue")
    tess.fillcolor("purple")

    bars = [250, 200, 100, 99, 155, 19] # data here
    drawBar(tess, bars)
    wn.exitonclick()

if __name__ == "__main__":
    main()