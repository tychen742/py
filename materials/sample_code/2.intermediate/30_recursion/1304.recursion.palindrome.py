import string


def palindrome(s):
    line = ''
    for i in range(len(s)):
        if s[i] in string.ascii_letters:
            line = line + s[i]
    line = line.lower()
    # print(line)
    if len(line) > 1:
        if line[0] != line[-1]:  # base case here, stop clause
            return False

        else:  # calling self
            line = line[:0].replace(s[0], "") + line[1:]
            line = line[-1:].replace(line[-1], "") + line[:-1]
            return palindrome(line)
    return True


print('"kayak" iline a palindrome:', palindrome("kayak"))
print('"aibohphobia" is a palindrome:', palindrome('aibohphobia'))
print('"radar" is a palindrome:', palindrome('radar'))
print('"Kanakanak" is a palindrome:', palindrome('Kanakanak'))
print('"Wassamassaw" is a palindrome:', palindrome('Wassamassaw'))
print('"Viv" is a palindrome:', palindrome('Viv'))
print('"Live not on evil" is a palindrome:', palindrome('Live not on evil'))
print('"this is a test" is a palindrome:', palindrome("this is a test"))



# print (str[0])
# print (str[-1])
