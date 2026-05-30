import turtle

def drawPointedStar (tortoise, lineLength, numVertices):
    for i in range (5):
        for j in range (numVertices):
            tortoise.right(180 - 180 / numVertices)
            tortoise.forward(lineLength)
        tortoise.penup()
        tortoise.forward(350)
        tortoise.right(144)
        tortoise.pendown()

def main ():
    wn = turtle.Screen()
    wn.bgcolor("lightblue")
    tess = turtle.Turtle()
    tess.color("blue")
    tess.pensize(3)
    tess.speed(100)

    tess.penup()
    tess.setpos(-250, 0)
    tess.pendown()

    num_vertices = 5
    line_length = 100
    drawPointedStar(tess, line_length, num_vertices)

    wn.exitonclick()

if __name__ == '__main__':
    main()