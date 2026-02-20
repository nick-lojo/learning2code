# You're processing customer orders.
#
# You have an order dictionary:
# - order_id: 'ORD-1234'
# - customer: 'Sarah'
# - total: 89.99
#
# Try to retrieve the order's 'discount_code'.
# If that key doesn't exist, show the message 'No discount applied'.
#
# Make sure your code doesn't crash if the key is missing.

order = {
    'orderId':'ORD-123',
    'customer':'Sarah',
    'total':89.99
}

discount_code = order.get('discount code', 'There is no discount code for this order')
print(discount_code)