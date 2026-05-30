import random
import turtle

wn = turtle.Screen()
wn.setworldcoordinates(-1, -1, 1, 1)

fred = turtle.Turtle()
fred.up()
fred.speed(0)
# fred.hideturtle()
fred.ht()

numDarts = 500
insideCount = 0

# fred.tracer(100)

for i in range(numDarts):
    randx = random.random()
    randy = random.random()

    x = (randx - 0.5) * 2
    y = (randy - 0.5) * 2

    fred.up()
    fred.setposition(x, y)

    distance = fred.distance(0,0)
    if distance > 1 :
        fred.color("blue")
        fred.dot(5)
    else :
        fred.color("red")
        fred.dot(5)
        insideCount = insideCount + 1
    print(i)
# fred.update()

print(insideCount)
print(insideCount/numDarts * 4)

wn.exitonclick()