# You're tracking multiple products in inventory.
#
# Create three product dictionaries:
# Product 1: name='Keyboard', price=79, stock=12
# Product 2: name='Mouse', price=25, stock=35
# Product 3: name='Monitor', price=299, stock=8
#
# Store all three dictionaries in a list called products.
#
# Loop through the list and print each product's name and price.

product_1 = {
    'name':'keyboard',
    'price':79,
    'stock':12
}

product_2 = {
    'name':'mouse',
    'price':25,
    'stock':35
}

product_3 = {
    'name':'monitor',
    'price':299,
    'stock':8
}

products = [product_1, product_2, product_3]

for product in products:
    name = f"{product['name']}"
    print(f'\nName: {name.title()}')
    print(f"\tPrice: ${product['price']}")