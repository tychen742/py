# 0. create the list
fruits = ['apple', 'banana', 'cherry']
print("0. list", fruits)

# 1. append()
fruits.append('durian')
print("1. append: ", fruits)   # 1. ['apple', 'banana', 'cherry', 'durian']

# 2. insert()
fruits.insert(3, 'dragonfruit')
print("2. insert: ", fruits)

# 3. extend()
fruits2 = ['elder burry', 'fig']
fruits.extend()
print("3. extend", fruits)

# 4. index()
print("4. index: ", fruits.index("banana"))     #4. index: 1

nums = [1, 2, 3, 4, 9, 2, 2, 5, 6, 7]
# print("index(): ", nums.index(2, start=4, end=9))
print("4. index: ", nums.index(2, ))        #4. index: 5

# 5. count()
fruits.append("cherry")
print("5. count: ", fruits.count(''))

# 6. revers(0)
fruits.reverse()
print("6. reverse: ", fruits)

# 7. sort(0)
fruits.sort()
print("7. sort: ", fruits)

# 8. copy()
import copy
fruits_new_1 = fruits
fruits_new_2 = fruits.copy()
fruits_new_3 = copy.deepcopy(fruits)
print("8. copy: ", id(fruits))
print("8. copy: ", id(fruits_new_1))
print("8. copy: ", id(fruits_new_2))
print("8. copy: ", id(fruits_new_3))
print("8. copy: ", fruits is fruits_new_1)
print("8. copy: ", fruits is fruits_new_2)
print("8. copy: ", fruits is fruits_new_3)

num_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
num_list2 = list([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

num_list_deepcopy = copy.deepcopy(num_list)
print("num_list id: ", id(num_list))
print("num_list id: ", id(num_list_deepcopy))

# 9. remove()
fruits.remove('dragonfruit')
print(fruits)

# 10. pop()
fruits.pop(5)
print(fruits)
fruits.pop()
print(fruits)

# 11. clear()
