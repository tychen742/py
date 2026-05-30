# Lists and Strings are collections. Integers, float numbers, and boolean are primitive data type.
# print out lists with different Elements and nested list

import math

print()

# Lists
words = ["abc", "Washington", "Ethiopia"]
numbers = [1, 3, 6, 111]
mixed_list = [1, 3, "abc", [], False]

# nested_list = [words, numbers]
# print(nested_list)

# print(type (mixed_list))
# print(type (numbers))
# print(type(words))

print()

# Strings
# str_one = "this is ABC in the US of A"
# str_two = "1, 2, 3"
# print ("str_one:", type (str_one))
# print (type (str_two))

# numeric
num_1 = 123
print("type of 123", type(num_1))
# print ("length of integer", len (num_1))
##### NTS: integer data type has no length. Can not be counted.

num_2 = 1.23
print("type of 1.23", type(num_2))
# print ("length of 1.23", len (num_2))

##### NTS: float data type has no length. Can not be counted.

pi = math.pi
# print ("type of pi", len(pi))

# Tuple (will talk in a later chapter)
num_range = (1, 100, 12, 33, words)
print(num_range)
print(type(num_range))
print(len(num_range))
