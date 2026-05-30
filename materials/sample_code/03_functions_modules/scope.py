##### pay attention to x #####
x = 100
print(x, ", defined outside of function myfunc")

##### accessing global variables  
def func1():
    print("Accessed from outside of func1, x == ", x)    

func1()

##### change x 
x = 500

##### variable access inside a function
def func2():
    # print(x, "Changed ousside of fuction, x should be", x, "now.")
    x = 300
    print("Changed inside func2, x should == ", x, "now.")

func2()

##### function inside a function
def func3():
    x = 99
    def innerfunc():
        print(x, "in innerfunc")
        # x = 555
    
    innerfunc()
    print("Outside innerfunc, ", x)
func3()

print(x)