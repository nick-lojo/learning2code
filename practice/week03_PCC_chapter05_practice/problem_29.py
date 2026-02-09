ordered_items = ['shoes', 'gift card', 'backpack', 'water bottle', 'gift card']

for item in ordered_items:
    if item is 'gift card':
        print('Gift card will be sent via email')
    else:
        print(f'Shipping {item} to your address')