import turtle
import time

t = turtle.Turtle()

def forward_right_color(num_steps, degrees):

    for steps in range(num_steps):
        for c in ('blue', 'red', 'green'):
            t.color(c)
            t.forward (steps)
            t.right(degrees)

    time.sleep(5)
    turtle.clearscreen()
    turtle.mainloop()

def sun_flower(color, length, degrees):
    while True:
        t.color(color)
        t.forward(length)
        t.left(degrees)
        if abs(t.pos()) < 1:
            time.sleep(5)
            turtle.clearscreen()
            turtle.mainloop()
            break

sun_flower('red', 200, 170)

forward_right_color(100, 30)
