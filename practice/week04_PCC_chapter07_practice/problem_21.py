# You're building a cleanup tool for a hospital's supply inventory.
#
# A supply type was incorrectly entered multiple times and needs to be
# removed before the inventory is exported.
# Remove every instance of 'expired' from the list, then print the result.
#
# Inventory: ['gauze', 'expired', 'bandages', 'expired', 'gloves', 'expired']

inventory = ['gauze', 'expired', 'bandages', 'expired', 'gloves', 'expired']

while 'expired' in inventory:
    inventory.remove('expired')

print("Updated Inventory:")
for item in inventory:
    print(f"\t{item.title()}")