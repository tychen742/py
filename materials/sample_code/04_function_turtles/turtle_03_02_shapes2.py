import turtle as t



side = int(input("How many sides for the polygon: "))
length = int(input("Length of the side? (5 - 50): "))


t.bgcolor('orange')
t.shape('turtle')

def shape(side, length):
    for i in range (side):
        t.forward(length)
        t.left(360/side)


# shape(8, 50)



### housekeeping
t.exitonclick()
t.mainloop()