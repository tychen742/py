#!/usr/local/bin/python3.12

# # create a new list
fruits = ['apple', 'banana', 'cherry', "pineapple", "orange"]

# ## sort a list alphabetically
# # note that we are changing the list (lists are "mutable")
# fruits.sort()
# print(fruits)


# ## sort a numerical list
# nums = [1, 3, 9, 7, 5]
# nums.sort()
# print(nums)

# ## sort descenting
# nums.sort(reverse=True)
# print(nums)
# ## sort ascending
# nums.sort(reverse=False)
# print(nums)

# ## Sort with function
# def func(n):
#     # return (3 - n)        # 2, 0, -2, -1, 1   ==> [5, 4, 3, 2, 1]
#     return abs(3 - n)       # 2, 0, -2, -1, 1
# nums = [1, 3, 5, 4, 2]      # 2, 0, 2, 1, 1     ==> 3, 4, 2, 1, 5
# nums.sort(key=func)
# print(nums)
# # nums.sorted(key=func)
# # print(nums)

# ## sort is case sensitive
# fruits = ['apple', 'banana', 'Cherry', 'durian', 'Elderburry']
# fruits.sort()
# print(fruits)

# ## case-insensitive sort with .lower property
# ## https://docs.python.org/3/library/stdtypes.html?highlight=str%20lower#str.lower
# ## "eturn a copy of the string with all the cased characters 4 converted to lowercase."
# fruits = ['apple', 'banana', 'Cherry', 'durian', 'Elderburry']
# fruits.sort(key=str.lower)
# print(fruits)

# ## reserse sort
# fruits = ['apple', 'banana', 'Cherry', 'durian', 'Elderburry']
# fruits.reverse()
# print(fruits)

