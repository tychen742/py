### Lists are mutable, comparing to Strings
### Here we are assigning a change of element and keep the object fruit.
### We can not do this in String because Strings are immutable.

# Element Assignment
fruit = ["apple", "banana", "cherry"]
print(fruit)

fruit[0] = "pear"  # index 0 is the first one from left; not 1
fruit[-1] = "orange"  # This (index -1) would be the first one from right
print(fruit)

# Element Assignment + Slicing
alist = ['a', 'b', 'c', 'd', 'e', 'f']
alist[1:3] = ['x', 'y']
print(alist)

# use Slicing to remove elements
blist = ['a', 'b', 'c', 'd', 'e', 'f']
blist[1:3] = []
print(blist)

# slicing Elements using LIST into Empty Slice
alist = ['a', 'd', 'f']
alist[1:1] = ['b', 'c']  ### insert into the empty slice before Element 1
print(alist)
alist[4:4] = ['e']
print(alist)

#
alist = [1, 2, 3, 4, 5]
alist[2] = True
print(alist)

alist = [1, 2, 3, 4, 5]
# alist[2:2] = True
alist[2:2] = [True]
print(alist)
