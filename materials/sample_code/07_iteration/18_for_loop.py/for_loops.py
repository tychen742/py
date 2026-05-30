##### list: create a list
list_num = [1, 2, 3, 4, 5]
# print(list_num) ### check to see if the list works ### comment out when it works

print("\n")

##### for loop
for num in list_num:
    if num == 3:
        continue

    print(num, end=" ")

print("\n")

##### while loop
i = 0
while i < len(list_num):
    print(list_num[i], end=" ")
    i = i + 1
    if list_num[i] == 3:
        break

print("\n")


for i in range(2, 10):
    for j in range(2, 10):
        print(i,  "*",  j,  "=", i*j, end="\t")
    print()