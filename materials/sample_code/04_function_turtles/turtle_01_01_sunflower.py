#1/3#### import some stuff for us; we don't write all our cde
import turtle as t
import time


#2/3.#### this is a fuction. We define a function to reuse a piece of code
def sunflower(color, length, degree):

    t.speed(500)
    # fill_color = 'yellow'
    # t.fillcolor('orange')
    # t.color("red")
    # t.begin_fill()
    
                                ### using the arguments here
    while True:                 ### condition-based loop; works when true

        t.color(color)
        t.forward(length)
        t.left(degree)
        if abs(t.pos()) < 1:    ### position is at close to (0, 0), menaing it's back stop at home
            break               ### if that's true, break out of the while loop

    # t.end_fill()


    # time.sleep(5)
    # t.clearscreen()
    t.exitonclick()     ##### we use this built-in function to click exit
    t.mainloop()


#3/3.#### We are calling the fuction here
##### you may change the arguments here
sunflower('red', 200, 170)      ### color, length, degree
