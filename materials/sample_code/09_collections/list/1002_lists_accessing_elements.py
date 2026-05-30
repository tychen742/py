# accessing elements in lists

print()

# Lists
numbers = [1, 3, 6, 111]
words = ["abc", "Washington", "Ethiopia"]
mixed_list = [1, 3, "abc"]
nested_list = [words, numbers]
mixed_nested_list = [words, numbers, 1, 2, 3, [], True, False]

print("Accessing elements of lists:")
print("2nd element in list numbers:", numbers[1])
print("2nd element in list words:", words[1])
print("2nd element in list mixed_list:", mixed_list[1])
print("2nd element in list nested_list:", nested_list[1])
print("1st element in list mixed_list:", mixed_nested_list[0])
print("2nd element in list mixed_list:", mixed_nested_list[1])
print("3rd element in list mixed_list:", mixed_nested_list[2])
print("4th element in list mixed_list:", mixed_nested_list[3])
print("5th element in list mixed_list:", mixed_nested_list[4])
print("6th element in list mixed_list:", mixed_nested_list[5])
print("7th element in list mixed_list:", mixed_nested_list[6])
print("8th element in list mixed_list:", mixed_nested_list[7])
# print("9th element in list mixed list:", mixed_nested_list[8]) # out of range



print()

# Strings
str_one = "USA"
str_two = "1, 2, 3"
# print ("str_one:", type (str_one))
# print (type (str_two))
# print ("The 1st character of str_one is:", str_one[1])
print("The 1st character of str_one is:", str_one[0])

##### NTS: lists, like strings, count from 0.
##### NTS: to access elements in lists, use INDEX OPERATOR [], just like strings

numbers = [17, 123, 87, 34, 66, 8398, 44]
print(numbers[2])  # 87
print(numbers[9 - 8])  # 123
print(numbers[-2])  # 8398 or out of bound? => 8398
print(numbers[len(numbers) - 1])  # 44

# List manipulation
alist = [3, 67, "cat", [56, 57, "dog"], [], 3.14, False]
print(alist[2].upper())

# More on Index Operator
alist = [3, 67, "cat", [56, 57, "dog"], [], 3.14, False]
print(alist[2][0])
