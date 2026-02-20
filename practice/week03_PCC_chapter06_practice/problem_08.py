# You're tracking inventory for a store.
#
# Start with this inventory:
# - apples: 50
# - oranges: 30
# - bananas: 40
#
# A customer buys 10 apples and 5 bananas.
# Update the inventory to reflect these sales.
#
# Print the updated inventory.

inventory = {
    'apples':50,
    'oranges':30,
    'bananas':40
}

inventory['apples'] = inventory['apples'] - 10
inventory['bananas'] = inventory['bananas'] - 5

print(inventory)