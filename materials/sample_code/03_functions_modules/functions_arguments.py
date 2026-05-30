
### a function is a block of code which only runs when it is called
### a function can return data as a result
def my_function():
    print("Hello from a function")


my_function

### you can pass data, known as arguments, into a function
### arguments
def my_function(fname):
    print(fname + " Chen")

### call the function passing the argument
my_function("lucy")
my_function("luke")
my_function("Junior")


### keyword arguments
def func_child(child1, child2, child3):
    print("The youngest child is " + child3)

func_child("Lucy", "Luke", child3 = "Junior")


### default param value
def func_default_value(country="Taiwan"):
    print("I am from " + country)

func_default_value("Taiwan")


### arbitrary arguments: *args
def func_kid(*kids):
    print("The youngest kid is " + kids[2])

func_kid("Lucy", "Luke", "Junior")


### **kwargs
def func_kwargs_kid(**kid):
    print("The last name is " + kid["lname"])

func_kwargs_kid(fname="Junior", lname='Chen')


### passing list as argument
def func_pass_list(arg_list):
    for x in arg_list:
        print(x)

fruits = ["apple", "banana", "cherry"]
func_pass_list(fruits)


### return values
def func_return(para):
    return para * 5

print(func_return(5))

