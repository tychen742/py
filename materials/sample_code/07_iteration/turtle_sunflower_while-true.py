import turtle as t
import time


def sunflower(color, length, degree):

    t.speed(500)
    # fill_color = 'yellow'
    # t.fillcolor('orange')
    # t.color("red")
    # t.begin_fill()
    

    while True:

        t.color(color)
        t.forward(length)
        t.left(degree)
        if abs(t.pos()) < 1:
            break

    # t.end_fill()


    # time.sleep(5)
    # t.clearscreen()
    t.exitonclick()
    t.mainloop()


sunflower('red', 200, 170)
