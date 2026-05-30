import turtle as t
from random import random

t.shape('turtle')

for i in range(100):
    steps = int(random() * 100)
    angle = int(random() * 360)
    t.right(angle)
    t.fd(steps)
    if 0 <= angle <= 90:
        t.bgcolor("red")
    elif 90 < angle <= 180:
        t.bgcolor("blue")
    elif 180 < angle <= 270: 
        t.bgcolor("orange")
    else:
        t.bgcolor("black")

t.home()                    ##### brings the turtle home
t.exitonclick()             ##### you will like this
t.mainloop()                ##### same as turtle.done()
