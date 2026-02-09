restricted_items = ['lithium batteries', 'spray paint', 'fireworks']
cart_items = ['laptop', 'lithium batteries', 'desklamp', 'spray paint',
              'notebook']

for item in cart_items:
    if item not in restricted_items:
        print(f'{item.title()} ready for shipping')
    else:
        print(f'Cannot ship {item} to your region')