import turtle
import tkinter as TK

wn = turtle.Screen()
wn.bgcolor("green")
turt=[]
for i in range(10):
    tur = 't' + str(i)
    tur = turtle.Turtle()
    print(tur)
    turt += tur

# t1 = turtle.Turtle()
u = turtle.Turtle()

turt[1].left(90)
u.right(90)

turt[1].forward(100)
u.forward(100)

turt[1].left(90)
u.left(90)

turt[1].forward(100)
u.forward(100)

# wn.exitonclick()
# wn.bye()

# turtle.Screen().mainloop()
