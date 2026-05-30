def count_char(char, string):
    count = 0
    for ch in string:
        if ch == char:
            count = count + 1
    return count


print(count_char("a", "banana aaa"))

# send a string
# specify a letter
# detect how many times the letter appear in the string
