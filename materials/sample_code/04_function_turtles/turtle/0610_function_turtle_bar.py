import turtle

def drawBar(turtle, bar_list):
    # for i in range (bar_list):
    for i in bar_list:
        turtle.begin_fill()
        turtle.left(90)
        turtle.forward(i)
        turtle.write(str(i))
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

    bars = [100, 30, 70, 4, 35, 59] # data here
    drawBar(tess, bars)
    wn.exitonclick()

if __name__ == "__main__":
    main()