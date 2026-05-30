file = open("studentdata.txt", "r")
aline = file.readline()
while aline:
    items = aline.split()
    # dataline = items[0] + ','
    # print(dataline)
    # print (items)
    sum = 0
    # avg = 0
    for i in range(1, len(items)):
        sum = sum + int(items[i])
    avg = sum / (len(items) - 1)
    print(items[0], avg)
    aline = file.readline()

file.close()
