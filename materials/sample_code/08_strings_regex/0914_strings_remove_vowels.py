def remove_vowel(str_a):
    vowels = "aeiouAEIOU"
    new_string = ""
    # for chr in (vowels):
    for character in (str_a):
        if character not in vowels:
            new_string = new_string + character
            # print (new_string)
    return new_string


print(remove_vowel("This is the best of times; this is the worst of times."))
# print (new_string)

# accumulator: new_string = new_string + character
