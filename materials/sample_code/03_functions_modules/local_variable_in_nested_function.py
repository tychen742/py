# Can't reassign variable in inner function
def outer1():
    a = 0
    print("a is 0.")
    b = 1
    print("b is 1")

    def inner():
        print("a is still:", a)
        print("b is still:", b)
        # b = 4  # uncomment this will reassign b and cause error

    inner()
outer1()


# during static analysis, the interpreter determines that b is assigned to in inner,
# and that it is therefore a local variable of inner.
# The print line attempts to print the b in that inner scope before it has been assigned.
#  http://stackoverflow.com/questions/5218895/python-nested-functions-variable-scoping



# Can't change string in inner function
def outer2():
    string = "Old string"

    def inner():
        string = "Old string was changed to new string by a nested function!"

    inner()
    return string


print("outer2:", outer2())


# nonlocal keyword make it works
def outer3():
    string = "Old string"

    def inner():
        nonlocal string
        string = "Old string was changed to new string by a nested function!"

    inner()
    return string


print("outer3:", outer3())


# Function attribute will work, too
def outer4():
    string = "Old string"

    def inner():
        inner.string = "Old string was changed to new string by a nested function!"

    inner.string = ""
    inner()
    return inner.string


print("outer4:", outer4())
