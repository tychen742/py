### list slicing is the same as string slicing

a_list = ['a', 'b', 'c', 'd', 'e', 'f']
print(a_list[1:3])  # starts with one and count before 3
print(a_list[:4])  # starts with 0 and ends with 3
print(a_list[3:])  # starts with 3 until the end
print(a_list[:])  # from beginning to the end
print(a_list[:-1])  # until before the last one (-1)
print(a_list[-2:-1])  #
print(a_list[-5:-1])  #
print(a_list[-2:0])
print(a_list[0:0])
print(a_list[0:1])

alist = [3, 67, "cat", [56, 57, "dog"], [], 3.14, False]
print(alist[4:])

### Reviewing list slicing

str_a = "Tobeornottobethatisthequestion."
str_slice = str_a[0:9]
print(str_slice)

for char in str_a:
    print(char, end="")

print()

### string indexing
# count = 0
for i in range(len(str_a) - 1):
    if (str_a[i] + str_a[i + 1]) == "th":
        print(i)
        # count = count + 1
        # print (count)
