def add_fruit(inventory, fruit, quantity=0):
    if fruit not in (inventory):
        inventory.update({fruit: quantity})
        return inventory
    else:
        inventory[fruit] += quantity
        return inventory


new_inventory = {}
# new_inventory.update {}
print(add_fruit(new_inventory, 'strawberries', 10))

print('strawberries' in new_inventory)
print(new_inventory['strawberries'])
print(add_fruit(new_inventory, "strawberries", 25))
print(new_inventory["strawberries"])
