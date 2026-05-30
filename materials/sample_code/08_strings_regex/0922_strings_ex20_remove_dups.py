# give a string,
# create a new string by adding the characters that are not in the old string
import string


def remove_dups(oldString):
    newStr = ""
    alphabets = string.ascii_letters

    for char in alphabets:
        if char not in oldString:
            oldString = oldString + char
            newStr = oldString

    return newStr


def main():
    old_string = "abcdefghijklmnopqrstuvwxyz. "

    remove_dups(old_string)

    print(remove_dups(old_string))


if __name__ == '__main__':
    main()
