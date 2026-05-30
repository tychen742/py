print()
vals = ['aaa', 'bbb', 'ccc']

# loop through
print("The basics:")
for val in vals:
    print(val)

print()
print("I need the indices:")
for i in range(len(vals)):
    print(i, vals[i])


print()
print("enumerate is better: clear abt what we want")

for idx, val in enumerate(vals):
    print(idx, val)


print()
