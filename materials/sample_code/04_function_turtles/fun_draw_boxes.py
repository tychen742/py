import turtle


def draw_a_square(tess, length):
    tess.forward(length)
    tess.left(90)
    tess.forward(length)
    tess.left(90)
    tess.forward(length)
    tess.left(90)
    # tess.penup()
    tess.forward(length)
    tess.hideturtle()  # hide turtle


def shift_an_angle(tess, length, angle):
    for i in range(1, int(360 / angle)):
        draw_a_square(tess, length)
        tess.left(angle)


def main():
    wn = turtle.Screen()
    # wn.bgcolor("lightblue")
    tess = turtle.Turtle()
    # tess.color("blue")
    # tess.pensize(3)
    # tess.speed(100)

    # tess.penup()
    # tess.setpos(-250, 0)
    # tess.pendown()

    # num_vertices = 5
    line_length = 100
    degree = 10

    # draw_a_square(tess, line_length)
    shift_an_angle(tess, 100, 13)
    wn.exitonclick()


if __name__ == '__main__':
    main()
