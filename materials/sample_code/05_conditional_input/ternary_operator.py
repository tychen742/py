print()
print("A simple if statement:")

amount = 100
if amount > 50:
    raise_amount = 20
else:
    raise_amount = 10

print(raise_amount)

print()

print("ternary is better: concise")
amount = 100
raise_amount = 20 if amount > 50 else 10

print(raise_amount)

print()
