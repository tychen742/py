a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)
print(a is b)

### Now let's do aliasing:
a = b  ### a and b both refer to the a's copy of Collection of References
print(a == b)
print(a is b)
### a and b are now TWO reference collections pointing to the same objects

### Now let's change list a
a[1] = 0
### Let's test if a and b are still the same
print(a == b)
print(a is b)

### a and b stay the same because Lists are mutable.
### This is sometimes unexpected (and can be confusing) and may not be desirable behavior.

### ==> Don't alias with mutable objects.
### Strings and integers are safe to alias because they are immutable.

# test:
alist = [4, 2, 8, 6, 5]
blist = alist
blist[3] = 999
print(alist)
