import turtle
import time

t = turtle.Turtle()

def fun_shape(num_steps, degrees, dist):

    for steps in range(num_steps):
        for c in ('black', 'yellow'):
            if steps < 50 or steps > 150:
                t.color('yellow')
            else:
                t.color(c)
            t.forward (steps)
            t.right(degrees)

    turtle.mainloop()

fun_shape(200, 60, 10)