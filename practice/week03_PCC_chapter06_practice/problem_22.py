# You're checking product availability in a warehouse.
#
# You have a product dictionary:
# - product_id: 'PROD-789'
# - name: 'Wireless Headphones'
# - price: 129.99
#
# Try to retrieve the product's 'warehouse_location'.
# If that key doesn't exist, show the message 'Location not assigned'.
#
# Make sure your code doesn't crash if the key is missing.

product = {
    'product_id':'PROD-789',
    'name':'Wireless Headphones',
    'price':129.99
}

warehouse_location = product.get('location', 'Location not assigned')
print(warehouse_location)