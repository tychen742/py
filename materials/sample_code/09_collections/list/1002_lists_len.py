# print out length of lists with different Elements and nested list

print()

# Lists
numbers = [1, 3, 6, 111]
words = ["abc", "Washington", "Ethiopia"]
mixed_list = [1, 3, "abc"]
nested_list = [words, numbers]
mixed_nested_list = [words, numbers, 1, 2, 3, [], True, False]

print("length of lists:")
print("length of an integer list", len(numbers))
print("length of a string list", len(words))
print("length of a mixed list", len(mixed_list))
print("length of a nested list", len(nested_list))
print("length of a mixed element nested list", len(mixed_nested_list))

print()

# Strings
str_one = "this is ABC in the US of A"
str_two = "1, 2, 3"
# print ("str_one:", type (str_one))
# print (type (str_two))
