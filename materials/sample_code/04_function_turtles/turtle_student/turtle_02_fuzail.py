#import circle_task as c

#import time

#c.forward_right_color(100, 30)

from math import degrees
import turtle as t
import time

def forward_right_color(num_steps, degree):

    for steps in range(num_steps):
        for c in ('blue', 'red', 'green'):
            t.color(c)
            t.forward(steps)
            t.right(degree)

    time.sleep(5)
    t.clearscreen()
    t.mainloop()


#forward_right_color(100, 30)

def sunflower(color,length,degree):
    
    

    while True:
    
        t.color(color)
        t.forward(length)
        t.left(degree)
        if abs(t.pos()) <1:
            break
    
    time.sleep(5)
    t.clearscreen()
    t.mainloop()
    
sunflower('red', 200, 170)