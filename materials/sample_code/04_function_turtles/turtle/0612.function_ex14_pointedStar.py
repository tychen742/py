import turtle


def draw_pointed_star(tortoise, line_length, num_vertices):
    for i in range(num_vertices):
        tortoise.right(180 - 180 / num_vertices)
        tortoise.forward(line_length)


def main():
    wn = turtle.Screen()
    wn.bgcolor("lightblue")
    tess = turtle.Turtle()
    tess.color("blue")
    tess.pensize(3)
    tess.speed(100)

    num_vertices = 5
    line_length = 300
    draw_pointed_star(tess, line_length, num_vertices)

    wn.exitonclick()

if __name__ == '__main__':
    main()

# Write a non-fruitful function to draw a five pointed star, where the length of each side is 100 units
