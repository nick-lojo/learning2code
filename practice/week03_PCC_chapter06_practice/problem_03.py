# You're processing customer orders for a restaurant.
#
# Each order contains:
# - Customer name
# - List of items ordered
# - Table number
# - Special instructions (optional - some orders won't have this)
#
# Process these three orders:
#
# Order 1:
# - Customer: Sarah
# - Items: burger, fries, soda
# - Table: 5
# - Special: no onions
#
# Order 2:
# - Customer: Mike
# - Items: pizza, salad
# - Table: 3
# - (no special instructions)
#
# Order 3:
# - Customer: Jenny
# - Items: pasta, garlic bread, water
# - Table: 7
# - Special: extra cheese
#
# For each order, print:
# - Customer name and table number
# - Each item ordered (one per line)
# - Special instructions if they exist, or "No special requests" if they don't

orders = {
    'order_1':{
        'customer':'sarah',
        'items':['burger', 'fries', 'soda'],
        'table':5,
        'special':'no onions'
    },
    'order_2':{
        'customer':'mike',
        'items':['pizza','salad'],
        'table':3,
    },
    'order_3':{
        'customer':'jenny',
        'items':['pasta', 'garlic bread', 'water'],
        'table':7,
        'special':'extra cheese'
    }
}

for order, details in orders.items():
    order_number = f'{order.title()}'
    print(f'{order_number}:')

    customer = f"{details['customer']}"
    print(f'\tCustomer: {customer.title()}')

    print('\tItems:')
    for item in details['items']:
        print(f'\t\t{item.title()}')
    
    print(f"\tTable: {details['table']}")

    special = details.get('special')
    if special:
        print(f"\tSpecial instructions: {special}")
    else:
        print('\tNo special instructions')