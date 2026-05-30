
import turtle as t
import time

def forward_right_color(num_steps, degrees):

    for steps in range(num_steps):
        for c in ('blue', 'red', 'green'):
            t.color(c)
            t.forward (steps)
            t.right(degrees)

    time.sleep(5)
    t.clearscreen()
    t.mainloop()

forward_right_color(100, 30)

def sun_flower(color, length, degrees):
    while True:
        t.color(color)
        t.forward(length)
        t.left(degrees)
        if abs(t.pos()) < 1:
            time.sleep(5)
            t.clearscreen()
            t.mainloop()
            break

sun_flower('red', 200, 170)


