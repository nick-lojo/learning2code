# You're cleaning up a product inventory list before exporting it.
#
# A warehouse manager flagged 'discontinued' as an invalid entry
# that was accidentally added multiple times.
# Remove every instance of 'discontinued' from the list before export.
# Print the cleaned list when done.
#
# Inventory:
# ['widget', 'discontinued', 'gadget', 'discontinued', 'tool', 'discontinued']

inventory = ['widget', 'discontinued', 'gadget', 'discontinued', 'tool',
             'discontinued']

while 'discontinued' in inventory:
    inventory.remove('discontinued')
print(inventory)