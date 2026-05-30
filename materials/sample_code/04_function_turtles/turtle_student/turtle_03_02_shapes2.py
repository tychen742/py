import turtle as t

t.bgcolor('orange')
t.shape('turtle')

### the function
def shape(side = 8, length = 50):
    for i in range (side):
        t.forward(length)
        t.left(360/side)


side = int(input("How many sides for the polygon: "))
length = int(input("Length of the side? (5 - 50): "))

shape(side, length)


### housekeeping
t.exitonclick()
t.mainloop()        ### keep the window open
# t.done()            # same as t.screen.mainloop()
# t.bye()             # close the turtle graphics window
# t.clearscreen()    # clear the screen
# t.reset()          # clear the screen and reset the turtle