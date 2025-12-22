requested_toppings = []

#for topping in requested_toppings: #First attempt, incorrect
    #if topping in requested_toppings:
        #print(f'Adding {topping}')
    #else:
        #print('Are you sure you want a plain pizza?')

#Second attempt after checking notes

if requested_toppings:
    for topping in requested_toppings:
        print(f'Adding {topping}')
else:
    print('Are you sure you want a plain pizza?')