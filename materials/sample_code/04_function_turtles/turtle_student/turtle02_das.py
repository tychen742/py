import turtle as t
import time

# Turtle Task #2

# defining fuction that draws patterns based on number of steps and degrees
def forward_right_color(num_steps, degrees):
    for steps in range(num_steps):
        for c in ('blue', 'red', 'green'):
            t.color(c)
            t.forward(steps)
            t.right(degrees)

    time.sleep(5)
    t.clearscreen()
    t.mainloop()

# Turtle Task #3

# defining function that draws a colored sunflower like pattern
def sun_flower(color,length,degree):
    while True:
        t.color(color)
        t.forward(length)
        t.left(degree)
        if(abs(t.pos())<1):
            break

    t.mainloop()


# calling forward_right_color function
# num_steps = int(input("Enter a number of steps:"))
# degrees = int(input("Enter the angle in degrees:"))
# forward_right_color(num_steps,degrees)


# calling sun_flower function
sun_flower('blue',150,230)