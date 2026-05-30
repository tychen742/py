# 0. create the list
fruits = ['apple', 'banana', 'cherry']
print(fruits)

# 1. append()
fruits.append('durian')
print(fruits)

# 2. insert()
fruits.insert(3, 'dragonfruit')
print(fruits)

# 3. extend()
fruits2 = ['elder burry', 'fig']
fruits.extend(fruits2)
print(fruits)

# 4. index()
print(fruits.index("banana"))
nums = [1, 2, 3, 4, 5, 6, 7]
# print("index(): ", nums.index(2, start=2, end=6))
print(nums.index(3, 2, 6))

print(fruits.index('cherry'))

# 5. count()
fruits.append("cherry")
fruits.count('cherry')

# 6. revers(0)
fruits.reverse()
print(fruits)

# 7. sort(0)
fruits.sort()
print(fruits)

# 8. copy()
fruits_new = fruits.copy()
print(id(fruits))
print(id(fruits_new))
fruits_new_2 = fruits
print(id(fruits_new_2))

# 9. remove()
fruits.remove('dragonfruit')
print(fruits)

# 10. pop()
fruits.pop(5)
print(fruits)
fruits.pop()
print(fruits)

# 11. clear()
