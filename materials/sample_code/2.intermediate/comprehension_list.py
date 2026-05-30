print()

print("append to generate a list:")
squares = []
for i in range(1, 6):
    squares.append(i ** 2)

print(squares)

print()

print("list comprehension: simple and explicit")

squares = [i ** 2 for i in range(1, 6)]
print(squares)

print()