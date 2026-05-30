# in and not in are boolean operators for list membership

fruit = ["apple", "banana", "cherry"]

print("apple" in fruit)
print("pear" in fruit)
print("pear " not in fruit)
print("apple" in fruit)

# list membership of nested element
alist = [3, 67, "cat", [56, 57, "dog"], [], 3.14, False]
print(57 in alist)
print(56, 57, "dog" in alist)  ### this means 56, 57, and the dog membership
print([56, 57, "dog"] in alist)

# now let's do a review on string membership
astring = "This is a string."
print("This" in astring)
