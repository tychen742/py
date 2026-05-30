#1/3#### import some stuff for us; we don't write all our cde
import turtle as t
from time import sleep


#2/3.#### this is a fuction. We define a function to reuse a piece of code
def shape(length, degree, times):
    
    ### clear the canvas
    # t.clear()
    

    ### draw
    for i in range(int(times)):     ### i is the control variable
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

#3/3.#### We are calling the fuction here
shape(120, 97, 100) ### length, degree, times