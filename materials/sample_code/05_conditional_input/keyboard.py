import turtle
from random import randint
image = "turtle.gif"  # type: str
screen = turtle.Screen()
screen.title("THis is my Turtle!! ")

t = turtle.Turtle()
screen.register_shape("triangle",((5,-3), (3,5), (-5,-3), (-3, 5)) )

def up():
    t.setheading(90)
    t.forward(10)
def down():
    t.setheading(270)
    t.forward(10)
def left():
    t.setheading(180)
    t.forward(10)
def right():
    t.setheading(0)
    t.forward(10)

def aliens():
    while True:
        ### generate one alien on rand position at rand time
        ### move the alien down
        alien = randint()



screen.onkey(up, "Up")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.onkey(down, "Down")

screen.listen()

# screen.mainloop()

screen.exitonclick()

