# # #!/usr/local/bin/python3.12

# loop through with index
fruits = ['apple', 'banana', 'cherry']
for index in range(len(fruits)):
    print(fruits[index])

# loop through with index numbers and range
fruits = ['apple', 'banana', 'cherry']
for index in range(len(fruits)):
    print(fruits[index])

# loop through list
nums = [1, 2, 3, 4, 5]
for num in nums:
    print(num)

# loop through with a While loop
print()
print("while loop:")
fruits = ['apple', 'banana', 'cherry']

i = 0
while i < len(fruits):
    print(fruits[i])
    i = i + 1

print()
# loop through with List Comprehension
print("List Comprehension:")
fruits = ['apple', 'banana', 'cherry']
[print(x) for x in fruits]