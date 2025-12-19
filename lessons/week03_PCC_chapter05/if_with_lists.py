#Using if statements inside a for loop to handle special items

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print(f'Adding {requested_topping}.')

print('\nFinished making your pizza!')

#Handling a special case - pizzeria runs out of green peppers

requested_toppings = requested_toppings[:]

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print('Sorry, we are out of green peppers right now.')
    else:
        print(f'Adding {requested_topping}')

print('\nFinished making your pizza!')

#Checking that a list is not empty before looping
#Empty list evaluates to False in an if statement

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f'Adding {requested_topping}.')
    print('\nFinished making your pizza!')
else:
    print('Are you sure you want a plain pizza?')

#Using multiple lists - check if requested items are available

available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f'Adding {requested_topping}.')
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print('\nFinished making your pizza!')