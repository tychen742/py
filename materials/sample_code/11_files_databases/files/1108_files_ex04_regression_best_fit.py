import turtle

file = open("labdata.txt", "r")


def draw_xy(w, t, coordX, coordY):
    # items = list(map(int, items))
    # items = int(items)
    # for value in (coordinates):
    # print (coordinates, 'test')
    for i in range(len(coordX)):
        X = int(coordX[i])
        Y = int(coordY[i])
        t.penup()
        t.goto((X), (Y))
        t.stamp()
        # coordX = tempX + coordX
        # coordY = tempY + coordY

        # print (type(coordX))
        # print ('coords in draw:', coordX, coordY)


def draw_best_fit(w, t, coordx, coordy):
    print("test draw_best_fit")  # print many times????? ### called many times!!!
    # print (x)
    # print (y)
    # avg_x = avg(x)
    avg_x = sum(coordx) / len(coordx)
    print('avg_x:', avg_x)
    avg_y = sum(coordy) / len(coordx)
    print('avg_y:', avg_y)
    sum_1 = 0
    sum_2 = 0
    # constant_m = 0
    for i in range(len(coordx)):
        sum_1 = (sum_1 + ((coordx[i] * coordy[i]) - len(coordx) * avg_x * avg_y))
    print('sum_1:', sum_1)
    for i in range(len(coordy)):
        sum_2 = sum_2 + ((coordx[i] ** 2) - len(coordy) * (avg_x ** 2))
    print('sum_2:', sum_2)
    # print (sum_1/sum_2)
    constant_m = sum_1 / sum_2
    # return 0.0
    ### equation y = avg_y + m (x - avg_x)
    point_1_y = avg_y + constant_m * (0 - avg_x)  ### x = 0
    print(point_1_y)
    point_2_y = avg_y + constant_m * (max(coordx) - avg_x)
    print(point_2_y)

    t.color("red")
    t.setpos(0, point_1_y)
    t.pendown()
    t.setpos(max(coordx), point_2_y)
    t.penup()


def plotRegression():
    aline = file.readline()
    wn = turtle.Screen()
    tess = turtle.Turtle()
    tess.shape("circle")
    tess.shapesize(0.25)
    # coordX = 0
    # coordY = 0

    for i in range(4):
        tess.forward(200)
        tess.backward(200)
        tess.left(90)
    coordX = []
    coordY = []

    while aline:
        items = (aline.split())
        # print (type(items))   # list type
        # print ('one, two:', items)    # while print ['x', 'y'] list line by line
        # coordX = []   # Can't put here, must be outside of the loop
        # coordY = []
        for i in range(len(items)):  # list comprehension
            #     # print ('test plot')
            coord = int(items[i])
            # print ('original coords', coord)    # one by one, x, y, x, y, ...
            # print (type (coord))              # made sure int
            if (i % 2) == 0:
                # print (type (items[i]))   # string
                # coord_X.append(items[i])
                coordX.append(coord)
                # print ('coord_X:', coordX)
            else:
                coordY.append(coord)
                # print ('coord_Y', coordY)
        draw_xy(wn, tess, coordX, coordY)

        aline = file.readline()
    draw_best_fit(wn, tess, coordX, coordY)

    wn.exitonclick()  # align with the wn created up there


def main():
    plotRegression()  ### SHOULD pass data as an argument from here.


if __name__ == '__main__':
    main()

    file.close()
