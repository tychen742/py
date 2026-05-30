file = open("alice's_adventures_in_wonderland.txt", "r")
aline = file.readline()
words = {}


def add_word(dict, word, quantity=1):
    if word not in dict:
        dict.update({word: quantity})
    else:
        dict[word] += quantity
    return dict


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


def lengths(words):
    longest = 0
    for key, value in (words.items()):
        # print (key)
        if len(key) > longest:
            longest = len(key)
    return longest


print(lengths(words))

for key, value in words.items():  ### note that here items() method takes 2 arguments
    # print (len(key))
    if len(key) == (lengths(words)):
        print('the long one(s):', key)
