import turtle as t
import calc

t.bgcolor('orange')
t.shape('turtle')
# t.speed(250)


def drawBar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.left(90)               # Point up
    t.forward(height)        # Draw up the left side
    t.right(90)
    t.forward(40)            # width of bar, along the top
    t.right(90)
    t.forward(height)        # And down again!
    t.left(90)               # put the turtle facing the way we found it.



# xs = [48, 117, 200, 240, 160, 260, 220]

# for v in xs:                 
#     drawBarA(t, v)



# Driver Code


a_list = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 5, 1, 2, 2, 2, 3, 3, 
          3, 3, 4, 4, 5, 1, 2, 2,  3, 3, 4, 4, 5, 1, 2, 2, 2, 3, 
          3, 3, 3, 4, 4, 5, 1, 2, 2,  3, 3, 4, 4, 5, 1, 2, 2, 2, 
          3, 3, 3, 3, 4, 4, 5, 1, 2, 2,  3, 3, 4, 4, 5, 1, 2, 2,
          2, 3, 3, 3, 3, 4, 4, 5, 1, 2, 2,  3, 3, 4, 4, 5, 1, 2, 
          2, 2, 3, 3, 3, 3, 4, 4, 5, 1, 2, 2,  3, 3, 4, 4, 5, 1, 
          2, 2, 2, 3, 3, 3, 3, 4, 4, 5, 1, 2, 2,  3, 3, 4, 4, 5, 
          1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 5, 1, 2, 2,  3, 3, 4, 4, 
          5, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 5, 1, 2, 2,  3, 3, 4, 
          4, 5, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 5, 1, 2, 2,  3, 3, 
          4, 4, 5, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 5, 1, 2, 2,  3, 
          3, 4, 4, 5, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 5, 1, 2, 2,  
          3, 3, 4, 4, 5, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 5, 1, 2, 2,  
          3, 3, 4, 4, 5, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 5, 1, 2, 2,  
          3, 3, 4, 4, 5, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 5, 1, 2, 2,  
          3, 3, 4, 4, 5, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 5, 1, 2, 2,  
          3, 3, 4, 4, 5, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 5, 1, 2, 2, 
          2, 3, 3, 3, 3, 4, 4, 5, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 5, 
          1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 5, 1, 2, 2, 2, 3, 3, 3, 3, 
          4, 4, 5, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 5, 1, 2, 2, 2, 3, 
          3, 3, 3, 4, 4, 5]

a_dic = (calc.freq(a_list))
# print(a_dic)
lst = list(a_dic.values())
# print(lst)

# def draw():
for v in lst:
    drawBar(t, v)


# housekeeping
t.exitonclick()
# t.done()
# t.mainloop()


# ### what is __name__ == '__main__'? see: https://realpython.com/if-name-main-python/
# ### main as the entry point in Java

if __name__ == '__main__':
    print("Okay")