def mirror_string(old_string):
    new_string = ""
    length = len(old_string)
    for i in range(0, int(length)):
        new_string = old_string[i] + new_string

    return (old_string + new_string)


string_a = "Python"

print(mirror_string(string_a))
