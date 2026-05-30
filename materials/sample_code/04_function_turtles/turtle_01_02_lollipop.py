#1/3#### import some stuff for us; we don't write all our cde
import turtle as t
import time

t.shape('turtle')
t.speed(100)


#2/3.#### this is a fuction. We define a function to reuse a piece of code
def forward_right_color(num_steps, degree):

    for steps in range(num_steps):              ### start with step 0 until...
        for c in ('blue', 'red', 'green'):      ### for each step, do the three colors...
            t.color(c)
            t.forward(steps)
            t.right(degree)

    # time.sleep(5)
    # t.clearscreen()
    ### making the stick
    t.home()
    t.up()
    t.down()
    t.right(90)
    t.fd(250)
    t.exitonclick()
    t.mainloop()


#3/3.#### We are calling the fuction here
forward_right_color(10, 40)     ### passing num_steps, degree to function
