# You're tracking inventory updates.
#
# Start with this inventory:
# - 'hammer': 15
# - 'screwdriver': 22
# - 'wrench': 8
#
# A shipment arrives with 10 more hammers.
# A customer buys 3 wrenches.
# You discontinue screwdrivers (remove from inventory).
#
# Print the updated inventory showing each tool and its quantity.

inventory = {
    'hammer':15,
    'screwdriver':22,
    'wrench':8
}

inventory['hammer'] = inventory['hammer'] + 10
inventory['wrench'] = inventory['wrench'] - 3
inventory['screwdriver'] = 0
del inventory['screwdriver']

print('Updated Inventory')
for tool, amount in inventory.items():
    print(f"\nTool: {tool.title()}")
    print(f"\tAmount in Stock: {amount}")