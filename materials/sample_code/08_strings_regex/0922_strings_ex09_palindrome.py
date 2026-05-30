def reverse_string(old_string):
    new_string = ""
    for ch in old_string:
        new_string = ch + new_string

    return new_string


def is_palindrome(myStr):
    if (reverse_string(myStr) == myStr):
        return True
    else:
        return False


string_a = "madam"

print(is_palindrome(string_a))
