# ######### WORKING CODE ######################
# infile = open('C://Users/tc16k/Downloads/pg288.txt', 'r')
# outfile = open('newbigfile.txt', 'a')  # CHANGED from 'w' (WRITE) to 'a' (APPEND)

# for i in range(10):
#     for line in infile:
#         print(line, file=outfile, end='')
# ######### WORKING CODE ######################


buffersize = 100000
infile = open('newbigfile.txt', 'r')
outfile = open('save_as_new_file.txt', 'w')
buffer = infile.read(buffersize)
bufferlimit = 10000000
i = 1
while bufferlimit > 0:
    outfile.write(buffer)
    print(i )
    i = i + 1
    bufferlimit = bufferlimit - buffersize
