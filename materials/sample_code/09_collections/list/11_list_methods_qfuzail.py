# 0. create the list
fruits = ['apple', 'banana', 'cherry']
print("0. list: ", fruits)          # list: ['apple', 'banana', 'cherry']

# 1. append()
fruits.append('durian')
print("1. append: ", fruits)        # 1. ['apple', 'banana', 'cherry', 'durian']

# 2. insert()
fruits.insert(3, 'dragonfruit')     # 2. insert:  ['apple', 'banana', 'cherry', 'dragonfruit', 'durian']
print("2. insert: ", fruits)

# 3. extend()
fruits2 = ['elder burry', 'fig']
fruits.extend(fruits2)
print("3. extend", fruits)  # extend ['apple', 'banana', 'cherry', 'dragonfruit', 'durian', 'elder burry', 'fig']

# 4. index()
print("4.1 index: ", fruits.index("banana"))        #4. index: 1

nums = [1, 2, 3, 4, 9, 2, 2, 5, 6, 7]
# print("index(): ", nums.index(2, start=4, end=9))
print("4.2 index: ", nums.index(2, 4, 7))           #4. index: 5

# 5. count()
fruits.append("cherry")
print("5. count cherry: ", fruits.count('cherry'))  # 5. count cherry:  2

# 6. revers(0)
fruits.reverse()
print("6. reverse: ", fruits)   # 6. reverse:  ['cherry', 'fig', 'elder burry', 'durian', 'dragonfruit', 'cherry', 'banana', 'apple']

# 7. sort(0)
fruits.sort()
print("7. sort: ", fruits)  # 7. sort:  ['apple', 'banana', 'cherry', 'cherry', 'dragonfruit', 'durian', 'elder burry', 'fig']

# 8. remove()   # remove by single value
fruits.remove('dragonfruit')
print("8. remove dragonfruit: ", fruits)

# 9. pop()      # remove by index
fruits.pop(5)
print("9.1 pop index 5", fruits)    # 9.1 pop index 5 ['apple', 'banana', 'cherry', 'cherry', 'durian', 'fig']
del fruits[3]
print("9.2 del index 3", fruits)    # 9.2 del index 3 ['apple', 'banana', 'cherry', 'durian', 'fig']


# 10. clear()
fruits.clear()
print("10. clear: ", fruits)    # [] empty list

# 11. copy()    # observe
fruits = ['apple', 'banana', 'cherry']
# print("11. type before extend", type(fruits))   # list
# fruits = fruits.extend(['X', "Y", "Z"])
# print("11. type after extend", type(fruits))    # NoneType
fruits_assign = fruits
fruits_copy = fruits.copy()   # for simpe objects
import copy
fruits_copy_copy = copy.copy(fruits)    # for compound objects
# fruits_deepcopy = copy.deepcopy(fruits)

print("11.1 id fruits: ", id(fruits))
print("11.1 id fruits_assign: ", id(fruits_assign))
print("11.2 id fruits_copy: ", id(fruits_copy))
# fruits_copy.append("XYZ")
# print("11.XYZ: ", fruits)
print("11.3 id fruits_copy_copy: ", id(fruits_copy_copy))
# print("11.4 id fruits_deepcopy: ", id(fruits_deepcopy))
print("11.5 fruits is fruits_assign: ", fruits is fruits_assign)
# print("11.6 copy: ", fruits is fruits_copy)
print("11.7 fruits is fruits_copy_copy: ", fruits is fruits_copy_copy)
# print("11.8 fruits is ftuits_deepcopy: ", fruits is fruits_deepcopy)

num_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
num_list2 = list([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
num_list_deepcopy = copy.deepcopy(num_list)
print("11. num_list id: ", id(num_list))
print("11. num_list2 id: ", id(num_list2))
print("11. num_list_deepcopy id: ", id(num_list_deepcopy))
