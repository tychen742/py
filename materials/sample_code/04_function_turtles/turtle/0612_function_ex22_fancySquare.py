import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("red")
tess.shape("blank")


def drawSprite(t, num_legs, core_distance, length):
    for i in range(num_legs):
        t.penup()
        t.forward(core_distance)
        t.pendown()
        t.forward(length)
        t.penup()
        t.backward(length + core_distance)
        t.pendown()
        t.left(360 / num_legs)


# drawSprite (tess, 17, 20, 30)

def fancySquare(t, n):
    for i in range(n):
        t.forward(100)
        drawSprite(tess, 10, 10, 20)
        t.left(360 / n)


fancySquare(tess, 4)
window.exitonclick()