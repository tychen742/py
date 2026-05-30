import turtle, time, asyncio

def forward_right_color(num_steps, degrees):
    start_time = time.time()
    for steps in range(num_steps):
        for c in ('blue', 'red', 'green'):
            turtle.color(c)
            turtle.forward(steps)
            turtle.right(degrees)
        if time.time() - start_time >= 5:
            turtle.clearscreen()
            start_time = time.time()
        
def sun_flower(color,length,degree):
    while True:
        turtle.color(color)
        turtle.forward(length)
        turtle.left(degree)
        if abs(turtle.pos())<1:
            break

sun_flower('red',200,170)
forward_right_color(100,30)


