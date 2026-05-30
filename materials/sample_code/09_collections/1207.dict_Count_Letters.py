# use dictionary for this?

dict = {'a': 0, 'b': 0, 'c': 0, "d": 0, "e": 0, "f": 0, "g": 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0,
        'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
# dict = {'a': 0, 'b': 0, 'c': 0}
stringA = input('please input a string: ')
# print(stringA)


for letter in stringA:
    # print(letter)
    if letter.isupper():
        letter = letter.lower()
    # for key in dict:
    if letter in dict.keys():
        dict[letter] = dict[letter] + 1
        #     print(letter)
        # print(dict[letter])

# print(dict)

for aKey in dict.keys():
    print(aKey, dict[aKey])
