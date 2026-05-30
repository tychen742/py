import turtle as t
from time import sleep
def shape(length, degree, times):
    
    ### clear the canvas
    # t.clear()
    

    ### draw
    for i in range(int(times)):
        t.forward(int(length))
        t.left(int(degree))


    t.home()
    ### stop turtle to avoid window closing
    # t.done()

    # sleep(3)

    # t.clearscreen()
    t.exitonclick()

    t.mainloop()
    # t.done()

# t.done()
shape(125, 97, 10)