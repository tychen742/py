import turtle

tess = turtle.Turtle()
wn = turtle.Screen()
wn.setworldcoordinates(-300, -300, 400, 300)
file = open("mystery.txt", "r")

# aline = file.readline()
for aline in file:
    items = aline.split()
    if items[0] == 'UP':
        tess.penup()
    elif items[0] == 'DOWN':
        tess.pendown()
    else:
        tess.goto(int(items[0]), int(items[1]))

wn.exitonclick()

# import turtle
#
# file = open("mystery.txt", "r")
#
# # def draw(wn, t, x, y):
# #     t.goto(x, y)
#
# def data_processing (aline):
#     coord = []
#     while aline:
#         # print ((aline))    ### parsed as string
#         if aline == 'DOWN\n':
#             # print ("You are down!")
#             plot(aline, coord)
#         elif (aline == "UP\n"):
#             print ("You are up.")
#         else:
#             # aline = aline[:-2]
#             x = int(aline.split()[0])
#             y = int(aline.split()[1])
#             print ('x', x)
#             print ('y', y)
#
#             coord = [x, y]
#             plot (aline, coord)
#             # print (type (aline()[0]))
#             # print ((aline))
#             # aline = int (aline)
#             # for i in ((len(aline))):
#             # for item in aline:
#             #     print (item)
#         # items = (aline.split())
#         # for item in (aline):
#         #     print ('items[i]:', item)
#         aline = file.readline()
#
#
# def plot(aline, coord):
#     # aline = file.readline()
#     wn = turtle.Screen()
#     tess = turtle.Turtle()
#     tess.shape("circle")
#     tess.shapesize(0.25)
#     if aline == 'UP':
#         tess.penup()
#     elif aline == 'DOWN':
#         tess.pendown()
#     else:
#         tess.goto(coord)
#     # wn.exitonclick()  # align with the wn created up there
#
#
# def main():
#     aline = file.readline()
#     data_processing(aline)
#     # plot()  ### SHOULD pass data as an argument from here.
#
#
# if __name__ == '__main__':
#     main()
#
#     file.close()
