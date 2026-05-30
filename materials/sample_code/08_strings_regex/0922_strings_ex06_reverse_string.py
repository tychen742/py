def reverse_string(old_string):
    new_string = ""
    for ch in old_string:
        new_string = ch + new_string

    return new_string


string_a = "“Hope” is the thing with feathers."

print(reverse_string(string_a))
