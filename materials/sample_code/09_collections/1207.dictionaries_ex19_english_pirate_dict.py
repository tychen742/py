file = open("english_pirate_dict.txt", "r")
aline = file.readline()

# make dict
dict = {}
for aline in file:
    # print (aline)
    aline = aline.split()

    for word in aline:
        # print (char)
        # print (type(aline))
        key = aline[0]
        # print ('key data typ:', type (key))
        if len(aline) == 2:
            value = aline[1]
        else:
            value = aline[1:]
        # print ('value data type:', type(value))
        dict.update({key: value})
        # print (dict)
# print (dict)

# input a sentence
user_str = input('Please input a sentence: ')

# check dict & # replace words
user_str = user_str.split()
# print ('type of user_string:', type(user_str))
# for word in user_str:
# print ('word in user_str:', word)

new_string = ''
for word in user_str:
    # print (word)
    if word in dict.keys():
        # if key == word:
        new_string += ''.join(dict[word]) + ' '.join([' '])
        # print (type(dict[word]))
    else:
        new_string += (word) + ' '

# print old and new sentences
print(new_string)
