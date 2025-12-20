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

#TRY IT YOURSELF

#5-8 Hello Admin

usernames = ['admin', 'user_1', 'user_2', 'user_3', 'user_4']

for username in usernames:
    if username == 'admin':
        print(f'Hello {username}, would you like to see a status report?')
    else:
        print(f'Hello {username}, thank you for logging in again.')

#5-9 No Users

usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print(f'Hello, {username}, would you like to see a status report?')
        else:
            print(f'Hello {username}, thank you for logging in again.')

else:
    print('We need to find some users!')

#5-10 Checking Usernames

current_users = ['User_1', 'USER_2', 'user_3', 'user_4', 'user_5']

new_users = ['user_6', 'user_7', 'user_8', 'USER_1', 'User_2']

current_users_lower = [user.lower() for user in current_users]

for username in new_users:
    if username.lower() in current_users_lower:
        print(f'{username}, already taken. Please select a different username.')
    else:
        print(f'{username} is available, would you like to proceed?')

#5-11 Ordinal Numbers

ordinal_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in ordinal_numbers:
    if number == 1:
        print(f'{number}st')
    elif number == 2:
        print(f'{number}nd')
    elif number == 3:
        print(f'{number}rd')
    else:
        print(f'{number}th')