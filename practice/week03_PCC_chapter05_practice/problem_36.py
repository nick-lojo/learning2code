prices = [5, 45, 75, 150, 8, 120]

for price in prices:
    if price < 10:
        print('Budget')
    elif price <= 49:
        print('Standard')
    elif price <= 99:
        print('Premium')
    elif price >= 100:
        print('Luxury')