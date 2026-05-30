file = open("studentdata.txt", "r")
aline = file.readline()
while aline:
    items = aline.split()
    new_items = items[1:]
    # for i in range (1, len(new_items)):
    print(items[0], min(new_items), max(new_items))
    aline = file.readline()

file.close()
