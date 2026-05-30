str = "apple"
for index in (str):
    print(index, "\t", end=" ")
print()

for index in range(len(str)):
    # print (index, end = " ")
    print(str[len(str) - 1], end=" ")
print()

for index in range(len(str) - 1, -1, -1):
    print(str[index], end=" ")
print()

for index in range(len(str)):
    print(str[index], end=" ")
print()

for index in range(0, len(str), 1):  # range from, to, step
    print(str[index], end=" ")
print()

for index in range(len(str) - 1, -1, -1):
    print(str[index], end=" ")
