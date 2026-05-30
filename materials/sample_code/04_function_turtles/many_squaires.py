##### function calls function

import turtle as t
t.shape("turtle")


def draw_square(t, size):
    for _ in range(4):
        t.forward(size)
        t.right(90)

# draw_square(t, 100)

# t.done()
# t.mainloop()
# t.exitonclick()


def draw_n_squares(t, size, count):
    for _ in range(count):
        draw_square(t, size)
        # t.right(360 / count)
        # size += 10
        # t.forward(10)
        # t.right(360 / count)
        t.right(360/count)


# draw_n_squares(t, 100, 10)
draw_n_squares(t, 100, 100)

t.exitonclick()
