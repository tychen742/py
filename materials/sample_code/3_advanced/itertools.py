print()
print("this does the job:")
colors = ['Red', 'Green']
sizes = ['S', 'M', 'L']

for color in colors:
    for size in sizes:
        print(color, size)
        
print()
print("itertools.product() (Cartesian Product) unpack the values in a single loop")
print("this gives us all possible combinations of two sets")
from itertools import product        
for color, size in product(colors, sizes):
    print(color, size)