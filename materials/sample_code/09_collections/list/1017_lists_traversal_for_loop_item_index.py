# List Traversal can be done BY ITEM or BY INDEX.

# By Item
fruits = ["apple", "banana", "cherry"]

for afruit in fruits:
    print(afruit)

for i in range(len(fruits)):  ### Don't forget the RANGE.
    """ The range here can be any SEQUENCE TYPE: list, tuple, range. """
    print(fruits[i])
