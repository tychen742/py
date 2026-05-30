# character classifications --> substitution cipher --> substitution decipher
import string  # don't forget to import string module

lower = string.ascii_lowercase
upper = string.ascii_uppercase


def cipher(toEncrypt, encryptMap):
    # pos = 0  # no need for this declaration. It's a temporary variable.
    newStr = ""
    for char in toEncrypt:  # take one character from toEncrypt
        if char in lower:
            pos = lower.index(char)
            newStr = newStr + encryptMap[pos]
        elif char in upper:
            pos = upper.index(char)
            newStr = newStr + encryptMap[pos + 26]
        elif char in string.punctuation:
            newStr = newStr + char
        elif char == " ":
            newStr = newStr + " "
    return newStr


def decipher(toDecipher, originalMap, encryptMap):
    newStr = ""
    for char in toDecipher:
        if char in encryptMap:
            pos = encryptMap.index(char)
            newStr = newStr + originalMap[pos]
        elif char in string.punctuation:
            newStr = newStr + char
        elif char == " ":
            newStr = newStr + " "
    return newStr


def main():
    originalNap = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encryptMap = "beafcgijldmnkohpqrtsuvwzyxBEAFCGIJLDMNKOHPQRTSUVWZYX"
    # toEncrypt = "She rose to His Requirement – dropt; The Playthings of Her LifeTo take the honorable Work; Of Woman, and of Wife -"
    toEncrypt = "This is a good test. Ha!"
    print(cipher(toEncrypt, encryptMap))

    # toEncrypt = "abcd,,hEF"
    # cipher(toEncrypt, letterMap)
    # toDecipher = "Sjlt lt b ihhf scts. Jb!"

    # print (decipher(toDecipher, originalNap, encryptMap))
    result = decipher(cipher(toEncrypt, encryptMap), originalNap, encryptMap)
    print(result)


if __name__ == '__main__':
    main()
