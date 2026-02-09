in_stock_items = ['laptop', 'mouse', 'keyboard', 'monitor']
customer_cart = ['LAPTOP', 'webcam', 'Mouse', 'headphones', 'KEYBOARD']

for item in customer_cart:
    if item.lower() in in_stock_items:
        print(f'Added {item.lower()} to cart.')
    else:
        print(f'{item.title()} is out of stock.')