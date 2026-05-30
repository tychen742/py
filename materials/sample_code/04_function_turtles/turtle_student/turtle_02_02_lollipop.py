import turtle as t
import time

t.shape('turtle')
t.speed(100)


def forward_right_color(num_steps, degree):

    for steps in range(num_steps):
        for c in ('blue', 'red', 'green'):
            t.color(c)
            t.forward(steps)
            t.right(degree)

    # time.sleep(5)
    # t.clearscreen()
    t.home()
    t.up()
    t.down()
    t.right(90)
    t.fd(250)
    t.exitonclick()
    t.mainloop()


forward_right_color(100, 40)
