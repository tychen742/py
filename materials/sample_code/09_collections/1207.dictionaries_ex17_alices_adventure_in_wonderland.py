file = open("alice's_adventures_in_wonderland.txt", "r")
aline = file.readline()


def add_word(dict, word, quantity=1):
    if word not in dict:
        dict.update({word: quantity})
    else:
        dict[word] += quantity
    return dict


line_count = 0
words = {}
for aline in file:
    aline = aline.lower()
    # print (aline) ### still sentence by sentence
    #
    # print (aline)
    aline = aline.split()
    # print (aline) ### still sentence by sentence
    for word in aline:
        # print (word)
        word = word.replace('_', '').replace('"', '').replace(',', '').replace('.', '')
        # word = word.replace('-', '').replace('?', '').replace('!', '').replace("'", "")
        word = word.replace('(', '').replace(')', '').replace(':', '').replace('[', '')
        word = word.replace(']', '').replace(';', '')
        if word.isalpha():
            add_word(words, word, 1)
            # print (type(aline))
            # line_count += 1


# print(line_count)
# print(words)

# keys = sorted(words.keys())
# for char in keys:
#     print(char, words[char])


def lengths(words):
    longest = 0
    for key, value in (words.items()):
        # print (key)
        if len(key) > longest:
            longest = len(key)
    return longest


print(lengths(words))

for key in words.items():
    if len(key) == 10:
        print('the longest:', key)
