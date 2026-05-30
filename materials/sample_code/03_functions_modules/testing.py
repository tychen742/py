# import numpy as np
# import jinja2
# import matplotlib as plt
#
# sentence = "Peter Piper picked a peck of pickled peppers A peck of pickled peppers Peter Piper picked If Peter Piper picked a peck of pickled peppers Wheres the peck of pickled peppers Peter Piper picked"
#
# word_dict = {}
#
# for word in sentence.split():
#     if word not in word_dict:
#         word_dict[word] = 1
#     else:
#         word_dict[word]+=1
#
# print(word_dict)
#
# def power(base, power):
#     result = base**power
#     return result
#
# def square(x):
#     result = power(x,2)
#     return result
#
# print(square( 3))

# import random
# import turtle   # turtle library
# screen = turtle.Screen()
# t = turtle.Turtle()  # create a turtle named t
# t.forward(100)
# t.left(90)
# t.forward(100)
# screen.exitonclick()
# # screen.bye()
#
# turtle.Screen().mainloop()

def test(num):
    if num < 10:
        return 0
    elif num < 20:
        return 1
    else:
        return 2

print(test(9))

new_string = ""
old_string = "iiiiiiiiiii"
for s in old_string:
    if s in "aeou":
        new_string = new_string + s
print(new_string)



