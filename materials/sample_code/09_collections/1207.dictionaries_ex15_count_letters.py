import string

input_str = input("Please input a sentence.")

char_upper = string.ascii_uppercase
char_lower = string.ascii_lowercase

dict = {}

# count = 0

input_str = input_str.lower()
for char in (input_str):
    # for ltr in char_lower:

    if char in char_lower:
        counts = input_str.count(char)
        dict.update({char: (counts)})
        # else:
        # count += 1
        # print ("something")

# print (dict)

keys = sorted(dict.keys())
# print (keys)
# keys.sort()

for char in keys:
    print(char, dict[char])
# for i in range (len(dict)+1):
# if dict [i] > dict [i+1]:
