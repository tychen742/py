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


def turtleMoving(wn, t):
    coin = random.randrange(0, 2)
    angle = random.randrange(0, 361)
    distance = random.randrange(0, 90)
    if coin == 0:
        t.left(angle)
        t.forward(distance)
    else:
        t.right(angle)
        t.forward(distance)


def main():
    wn = turtle.Screen()

    t1 = turtle.Turtle()
    t1.shape('turtle')
    t1.color("green")
    t1.up()
    t1.goto(random.randrange(-200, 200), random.randrange(-200, 200))
    t1.down()

    t2 = turtle.Turtle()
    t2.shape('turtle')
    t2.color("blue")
    t2.up()
    t2.goto(random.randrange(-200, 200), random.randrange(-200, 200))
    t2.down()

    while isInScreen(wn, t1) and isInScreen(wn, t2):
        turtleMoving(wn, t1)
        turtleMoving(wn, t2)

    wn.exitonclick()


if __name__ == '__main__':
    main()
