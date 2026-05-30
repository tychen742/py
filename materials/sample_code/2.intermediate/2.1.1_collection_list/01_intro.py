#0 
# ### Lists are one of 4 built-in data types in Python used to
# ### store collections of data, the other 3 are Tuple, Set, and Dictionary
# ### lists are indexed, ordered, changeable, and 
# ### allow duplicate values (as opposed to set and dictionary)
# ### Lists in Python are mutable


#1 
# ### creating a list
fruits = ['apple', 'banana', 'cherry']
nums = [ 111, 222, 333, 444, 555]
stuff = [ 1, 2, [3, 4, 5], 'python' ]

#2
# ### indexing
print(fruits[0])
print(stuff[2])
print(stuff[3])

#3 
# ### length of lists: the len() function
print(len(fruits))


# 4 data types
# ### lists can be of different data types
# 4.1 string
list_string = ['apple', 'banana', 'cherry']
# 4.2 numerical
list_integer = [ 1, 2, 3] 
# 4.3 boolean
list_bool = [True, False, True]


# 4.4 type()


###5 the list() Constructor
fruits = list(("apple", "banana", "cherry"))    ### a tuple as argument