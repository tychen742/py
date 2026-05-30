import turtle


def tree(branchLen, t):
    i = 0
    j = 0
    if branchLen > 5:
        t.forward(branchLen)
        print("moved forward:", branchLen)

        t.right(20)
        print("turned right 20 degree")

        print("calling tree function with:", branchLen)
        tree(branchLen - 15, t)

        t.left(40)
        print("turned left 40 degree")

        print("calling tree function with:", branchLen)
        tree(branchLen - 15, t)

        t.right(20)
        print("turned right 20 degree")

        t.backward(branchLen)
        print("moved backward:", branchLen)


def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75, t)
    myWin.exitonclick()


main()
