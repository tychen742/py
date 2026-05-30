import turtle as t
# from turtle import Turtle

# turtle = t.Turtle()
 
t.bgcolor('orange')
t.shape('turtle')
### square
for i in range(4):
    t.color('purple')
    t.forward(100)
    t.right(90)
     
### circle
t.teleport(100, 100)
t.circle(100)


### star
t.teleport(-200, -200)
t.right(75)
t.forward(100)

for i in range(4):
    t.right(144)
    t.forward(100)



### housekeeping
t.exitonclick()
t.done()            # same as t.screen.mainloop()



