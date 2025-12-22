available_toppings = ['mushrooms', 'olives', 'pepperoni']
requested_toppings = ['mushrooms', 'french fries', 'olives']

for topping in requested_toppings:
    if topping in available_toppings:
        print(f'Adding {topping}')
    else:
        print(f"Sorry, we don't have {topping}")
print('Pizza complete!')