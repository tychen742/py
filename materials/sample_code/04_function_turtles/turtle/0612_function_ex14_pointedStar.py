import turtle


def drawPointedStar (tortoise, lineLength, numVertices):
    for i in range (numVertices):
        tortoise.right(180 - 180 / numVertices)
        tortoise.forward(lineLength)

def main ():
    wn = turtle.Screen()
    wn.bgcolor("lightblue")
    tess = turtle.Turtle()
    tess.color("blue")
    tess.pensize(3)
    tess.speed(100)

    num_vertices = 5
    line_length = 300
    drawPointedStar(tess, line_length, num_vertices)

    wn.exitonclick()

if __name__ == '__main__':
    main()