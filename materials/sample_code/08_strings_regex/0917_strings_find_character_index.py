"""
Find and return the index of achar in astring.
Return -1 if achar does not occur in astring.
"""


def find(char, string):
    index = 0
    length = len(string)
    for i in range(length):
        if string[i] == char:
            # index = index + string[ch]
            # index = string[ch]
            # print(i)
            # index += 1
            # print (index)
            # return index
            return i  # when found, return
        else:
            # print ("eles")
            index = -1
    return index


print(find("C", "banana C"))
