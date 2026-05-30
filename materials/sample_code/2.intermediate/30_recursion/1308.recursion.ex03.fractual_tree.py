import random
import turtle


def angle():
    ang = random.randrange(15, 25)
    return ang


def cut_branch():
    cut = random.randrange(13, 17)
    return cut

def tree(branchLen, t, pensize):
    i = 0
    j = 0
    if branchLen > 5:
        t.pensize(pensize)
        if branchLen < 20:
            t.color('green')
        else:
            t.color('brown')
        t.forward(branchLen)
        t.right(20)
        tree(branchLen - cut_branch(), t, pensize - 3)
        t.left(40)
        if branchLen < 20:
            t.color('green')
        else:
            t.color('brown')
        tree(branchLen - cut_branch(), t, pensize - 3)
        t.right(20)
        t.penup()
        t.backward(branchLen)
        t.pendown()


def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("brown")
    pensize = 15
    tree(75, t, pensize)
    myWin.exitonclick()


main()
