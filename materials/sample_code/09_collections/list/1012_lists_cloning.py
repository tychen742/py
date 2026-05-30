a = [81, 82, 83]
b = a[:]  # make a clone using slice
print(a == b)  # still the same values
print(a is b)  # no longer the same object

b[0] = 5  # change in one object does not affect the other one

print(a)
print(b)
### This is what we usually expect: a and b are different lists.
### Aliasing can be confusing.
