# character classifications --> substitution cipher
import string  # don't forget to import string module

lower = string.ascii_lowercase
upper = string.ascii_uppercase


def cipher(toEncrypt, letterMap):
    # pos = 0  # no need for this declaration. It's a temporary variable.
    newStr = ""
    for char in toEncrypt:  # take one character from toEncrypt
        if char in lower:
            pos = lower.index(char)
            newStr = newStr + letterMap[pos]
        elif char in upper:
            pos = upper.index(char)
            newStr = newStr + letterMap[pos + 26]
        elif char in string.punctuation:
            newStr = newStr + char
        elif char == " ":
            newStr = newStr + " "
    return newStr


def main():
    # etterNap = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letterMap = "beafcgijldmnkohpqrtsuvwzyxBEAFCGIJLDMNKOHPQRTSUVWZYX"
    toEncrypt = "She rose to His Requirement – dropt; The Playthings of Her LifeTo take the honorable Work; Of Woman, and of Wife -"
    toEncrypt = "This is a good test. Ha!"
    # toEncrypt = "abcd,,hEF"
    # cipher(toEncrypt, letterMap)
    print(cipher(toEncrypt, letterMap))


if __name__ == '__main__':
    main()
