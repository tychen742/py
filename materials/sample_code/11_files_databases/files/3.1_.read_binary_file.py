buffersize = 100000
infile = open('C:/Users/tc16k/Downloads/keyboard.jpg', 'rb')   #  read from here
outfile = open('img/keyboard.jpg', 'wb')                  #  write to here
buffer = infile.read(buffersize)

# while len(buffer):
#     outfile.write(buffer)
#     buffer = input.read(buffersize)

while len(buffer):
    outfile.write(buffer)
    buffer = infile.read(buffersize)
