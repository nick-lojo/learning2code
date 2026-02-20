# You're tracking product inventory for a small store.
#
# Starting inventory:
# - laptop: 5 units
# - mouse: 20 units
# - keyboard: 15 units
#
# Today's transactions:
# - Sold 2 laptops
# - Sold 8 mice
# - Received shipment of 10 keyboards
# - Customer asked about 'monitor' stock (not in inventory)
#
# Build the system:
# - Start with the inventory dictionary
# - Process each transaction (update quantities)
# - When checking 'monitor', use a method that won't crash if key doesn't
#   exist
# - Print a message showing 'monitor' stock (should show 0 or appropriate
#   message)
# - Print final inventory showing each product and its quantity

inventory = {
    'laptop':5,
    'mice':20,
    'keyboard':15
}

inventory['laptop'] = inventory['laptop'] - 2
inventory['mice'] = inventory['mice'] - 8
inventory['keyboard'] = inventory['keyboard'] + 10

monitor = inventory.get('monitor', 'Monitors are not in stock.')
print(monitor)

print('Final Stock:')
for item, stock in inventory.items():
    print(f'\t{item.title()}: {stock}')