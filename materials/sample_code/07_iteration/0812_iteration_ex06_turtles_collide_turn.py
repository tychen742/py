import math
import random
import turtle


def moveX(angle, forward):
    radianValue = angle * 0.0174533
    moveXValue = (math.cos(radianValue) * forward)
    return moveXValue


def moveY(newAngle, forward):
    radianValue = newAngle * 0.0174533
    moveYValue = (math.sin(radianValue) * forward)
    return moveYValue


def isInScreen(w, t, newAngle, forward):
    leftBound = - w.window_width() / 2
    rightBound = w.window_width() / 2
    topBound = w.window_height() / 2
    bottomBound = -w.window_height() / 2

    moveXValue = moveX(newAngle, forward)
    print("moveXValue:", moveXValue)
    moveYValue = moveY(newAngle, forward)

    turtleX = t.xcor() + moveXValue
    print(t.xcor())
    print("predicted X", turtleX)
    turtleY = t.ycor() + moveYValue
    print(t.ycor())
    print("predicted Y", turtleY)

    if (turtleX > leftBound) and (turtleX < rightBound) and (turtleY < topBound) and (turtleY > bottomBound):
        print("True")
        return True
    else:
        return False


def moveTurtle(wn, t, newAngle, forward):
    t.left(newAngle)
    t.forward(forward)


def main():
    t = turtle.Turtle()
    w = turtle.Screen()
    t.shape("turtle")
    t.color("blue")

    newAngle = 0
    for i in range(10):
        print()
        print(i)

        angle = random.randrange(1, 361)
        print("angle =", angle)
        forward = random.randrange(0, 300)
        print("forward =", forward)

        # newAngle = newAngle + angle
        # newAngle = newAngle % 360
        print("angle:", angle)
        if isInScreen(w, t, angle, forward) == True:
            print("Move!")
            moveTurtle(w, t, angle, forward)
        else:
            print("don't move")

    w.exitonclick()


if __name__ == '__main__':
    main()
