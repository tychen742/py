def count_digit(num):
    # num_digit = len(num)          # TypeError: object of type 'int' has no len()
    num_digit = len(str(num))
    return num_digit


print(count_digit(10000))
