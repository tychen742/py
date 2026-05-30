input = open('text.txt', 'r')
output = open('new.txt', 'w')

for line in input:
    # print(line, end='')
    print(line, file=output, end='')