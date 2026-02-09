#Scenario 1

cart_items = []

if cart_items:
    for item in cart_items:
        print(f'Added item to cart: {item}')
    print('\nReady for checkout')
else:
    print('Your cart is empty. Please add items to continue')

#Scenario 2

cart_items = ['headphones', 'charger', 'case']

if cart_items:
    for item in cart_items:
        print(f'Added item to cart: {item}')
    print('\nReady for checkout')
else:
    print('Your cart is empty. Please add items to continue')