import random
import turtle


def isInScreen(w, t):
    leftBound = - w.window_width() / 2
    rightBound = w.window_width() / 2
    topBound = w.window_height() / 2
    bottomBound = -w.window_height() / 2

    turtleX = t.xcor()
    turtleY = t.ycor()

    stillIn = True
    if turtleX > rightBound or turtleX < leftBound:
        stillIn = False
    if turtleY > topBound or turtleY < bottomBound:
        stillIn = False

    return stillIn


def main():
    wn = turtle.Screen()
    t = turtle.Turtle()
    t.shape('turtle')

    while isInScreen(wn, t):
        coin = random.randrange(0, 2)
        angle = random.randrange(0, 361)
        distance = random.randrange(0, 90)
        if coin == 0:
            t.left(angle)
        else:
            t.right(angle)

        t.forward(distance)

    wn.exitonclick()


if __name__ == '__main__':
    main()
