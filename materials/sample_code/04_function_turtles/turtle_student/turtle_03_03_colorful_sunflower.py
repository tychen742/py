import turtle as t
import time


def sunflower(color, length, degree, fill_color='yellow', bg_color='purple'):

    t.speed(250)
    t.shape('turtle')

    t.bgcolor(bg_color)
    t.fillcolor(fill_color)

    t.begin_fill()

    while True:

        t.color(color)
        t.forward(length)
        t.left(degree)
        if abs(t.pos()) < 1:
            break

    t.end_fill()

    # time.sleep(5)
    # t.clearscreen()
    # housekeeping
    t.exitonclick()
    t.mainloop()


sunflower('red', 200, 170, 'black', 'orange')
