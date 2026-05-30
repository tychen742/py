### OPEN File with open()

qbfile = open('qbdata.txt', 'r')

for aline in qbfile:
    values = aline.split()
    print('QB', values[0], values[1], 'has a rating of', values[10])

qbfile.close()
