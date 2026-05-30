import turtle

def seq3np1(number):
    i = 0
    count = 0
    while number != 1:
        if number % 2 == 0:
            number = number / 2
        else:
            number = number * 3 + 1
        # print (number)
        count = count + 1
    return count

def main():
    wn = turtle.Screen()
    tess = turtle.Turtle()
    tess.penup()
    tess.setpos(-300, 0)
    tess.pendown()
    tess.pensize(3)
    tess.color("blue")

    maxSoFar = 0
    j = 0

    for i in range(2, 50):
        count = seq3np1(i)
        # print("It takes", count, "times.")

        if count > maxSoFar:
            maxSoFar = count
            j = i
        tess.penup()
        tess.right(90)
        tess.forward(15)
        tess.write(i)
        tess.backward(15)
        tess.pendown()

        tess.left(180)
        tess.forward(count)
        tess.write(count)
        tess.right(180)
        tess.forward(count)
        tess.left(90)

        tess.penup()
        tess.forward(10)
        tess.pendown()
    print("The #", j, "has the longest sequence", maxSoFar)
    wn.exitonclick()

if __name__ == '__main__':
    main()
