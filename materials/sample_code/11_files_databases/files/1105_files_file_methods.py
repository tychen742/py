qbfile = open('qbdata.txt', 'r')

###
# for aline in qbfile:
#     values = aline.split()
#     print ('QB', values[0], values[1], 'has a rating of', values[10])

### FOR iteratively parse in LINES as STRING
for aline in qbfile:
    values = aline.split()
    # print (aline)

### WHILE
infile = open("qbdata.txt", "r")

line = infile.readline()  ### read all lines from the file into a list, where each list element is one line
"http://stackoverflow.com/questions/9857104/assigning-multiple-lines-of-a-file-to-multiple-variables-using-readline-while"

while line:
    values = line.split()
    print('QB ', values[0], values[1], 'had a rating of ', values[10])
    line = infile.readline()

infile.close()

### READ() ==> entire file as a single STRING
qbfile = open('qbdata.txt', 'r')
print('read():', qbfile.read())

### READLINE() & READLINE(n)
qbfile = open('qbdata.txt', 'r')
print('readline():', qbfile.readline())  ### read one line
print('readline(10):', qbfile.readline(10))  ### marker
print('readline(10:', qbfile.readline(10))  ### marker

### READLINES() ==> LIST containing STRINGS\n
print('readlines LIST of STRINGS:', qbfile.readlines())  ###

qbfile.close()
