#  iterative function with accumulator variable

# sample iteration (for loop) with accumulator variable

accum_var = 0
for i in range(0, 10):
    accum_var = accum_var + i
    print(accum_var)


# turn the sample iteration into function
#  for loops needs to know the number of iterations, which is achieved by "len"
def list_sum(num_list):
    temp_sum = 0
    for i in range(0, len(num_list)):
        temp_sum = num_list[i] + temp_sum
        # print(temp_sum)
    return temp_sum


num_list = [1, 3, 5, 7, 9]


print(list_sum(num_list))


# add a list of number together using recursive calls
#  mathematical idea of recursive call: two terms in the expression

def sum_list(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + sum_list(num_list[1:])  # the two terms


print(sum_list(num_list))


#  convert base 10 integer to string
def convert(num, base):
    string_conversion = "0123456789ABCDEF"
    if num < base:
        return string_conversion[num]
    else:
        return convert(num // base, base) + string_conversion[num % base]


print(convert(10, 2))

# reverse a string using a recursion function

sample_string = "abcdefg"
iteration = len(sample_string) // 2


def reverse_loop(str):
    temp = ""
    for i in str:
        # temp = temp + i
        temp = i + temp
    return temp


print(reverse_loop("abc"))


def reverse_recursion(str):
    if len(str) == 0:
        return str
    else:
        return reverse_recursion(str[1:]) + str[0]


# remove white spaces in a string
str1 = "ab c d"
str1_new = ""
for i in range(len(str1)):
    if str1[i] == " ":
        continue
    else:
        str1_new = str1_new + str1[i]
print(str1_new)


# now turn it into a function
# use loop
def remove_spaces(s):
    str_spaces_removed = ""
    for i in range(len(s)):
        if (s[i] == " "):
            continue
        else:
            str_spaces_removed += s[i]
    return str_spaces_removed


print(remove_spaces("a a z"))


# now use recursion
def remove_whites(str):
    if len(str) == 0:
        return str
    else:
        if str[0] == " ":
            # pass
            return remove_whites(str[1:])
        else:
            return str[0] + remove_whites(str[1:])
    # return str


test_string = "a b csssss ss"
print(remove_whites(test_string))

if test_string[1] == " ":
    print("space test successful")

aaa = test_string[0]
print(aaa)
