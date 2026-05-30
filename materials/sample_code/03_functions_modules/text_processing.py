import re

file = open('/Users/tychen/Desktop/tt.txt', "r")

lines = file.readlines()

# num = 1
# for value in lines:
#    print(num, value)
#    num += 1

num = 1
empty = 0
for value in lines:
    # cancer_types = re.findall(r'"([^"]*)"', value)
    cancer_types = re.findall(r"'(.*?)'", value)
    print(num, cancer_types)
    num += 1
