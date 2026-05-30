# create a rot13 function using Caesar cipher.
import string


def rot13(theStr):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    newLetter = ""
    newStr = ""

    for char in theStr:
        if char in lower:
            pos = lower.index(char)
            if pos <= 13:
                newLetter = lower[pos + 13]
            else:
                newLetter = lower[pos + 13 - 26]
            newStr = newStr + newLetter
        elif char in upper:
            pos = upper.index(char)
            if pos <= 13:
                newLetter = upper[pos + 13]
            else:
                newLetter = upper[pos + 13 - 26]
            newStr = newStr + newLetter
        else:
            newStr = newStr + char
    return newStr


def main():
    theStr = "abc This is a good test. Capital test."
    print(rot13(theStr))


if __name__ == '__main__':
    main()
