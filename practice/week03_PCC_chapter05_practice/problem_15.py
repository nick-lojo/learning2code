requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for topping in requested_toppings:
    if topping == 'green peppers':
        print(f'Sorry, we are out of {topping}')
    else:
        print(f'Adding {topping}')
print('Pizza complete!')