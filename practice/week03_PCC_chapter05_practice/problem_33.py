order_total = 45
is_premium = True

if order_total >= 50 or is_premium:
    print('Free shipping applies')
else:
    print('Shipping fee: $5.99')