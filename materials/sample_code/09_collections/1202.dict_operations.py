inventory = {'apples': 100, 'banana': 200, 'cantelope': 300}
print(inventory)

inventory['apples'] = 300
print(inventory)

inventory['durian'] = 400
print(inventory)
print(len(inventory))

# update the value of one key
inventory['durian'] = inventory['durian'] + 600
print(inventory)

# but this is wrong
inventory = inventory['durian'] + 600
print(inventory)

# add the values together
aNum = inventory['apples'] + inventory['banana']
print(aNum)
