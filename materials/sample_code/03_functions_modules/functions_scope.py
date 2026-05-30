##### pay attention to x #####
x = 100
print("global scope: x ==", x)

# accessing global variables


def func1():
    print("inside func1, x == 100; check: x ==", x)


func1()

# change x
x = 500
print("blobal scope: reassign x = 500", "\n")

# variable access inside a function


def func2():
    # print(x, "Changed ousside of fuction, x should be", x, "now.")
    x = 300
    print("inside func2, reassign x as 300 , check: x ==", x)


func2()

# function inside a function


def func3():
    x = 99
    print("inside func3, reassign x as 99 , check: x ==", x)

    def innerfunc():
        x = 555
        print("inside func3/innerfunc, reassisgn x as 555, check: x ==", x)
        global y
        y = 777

    innerfunc()
    print("inside func3, after innerfuc, check: x ==", x, "\n")


func3()

print("global scope: x ==", x)
print("y is made global ==", y)
