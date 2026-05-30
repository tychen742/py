def remove_char(old_string, char):
    new_string = ""
    length = len(old_string)
    for i in range(0, int(length)):
        if old_string[i] != char:
            new_string = new_string + old_string[i]

    return (new_string)


string_a = "Python is the best programming language for social science."

print(remove_char(string_a, "s"))
