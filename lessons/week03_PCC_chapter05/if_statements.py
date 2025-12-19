#Simnple if statement - one test, one action
#If the test is True, Python executes the indented code
#If the test is False, Python ignores the indented code

age = 19
if age >= 18:
    print('You are old enough to vote!')

#Multiple lines can be indented under an if statement
#All indented lines execute if the test passes

age = 19
if age >= 18:
    print('You are old enough to vote!')
    print('Have you registered to vote yet?')

#if-else statment - handles both possibilities
#If test is True, run the if block
#If test is False, run the else block

age = 17
if age >= 18:
    print('You are old enough to vote!')
    print('Have you registered to vote yet?')
else:
    print('Sorry, you are too young to vote.')
    print('Please register to vote as soon as you turn 18!')

#if-elif-else chain - test multiple conditions
#Python runs tests in order and executes only the first one that passes

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f'Your admission cost is ${price}.')

#Using multiple elif blocks
#You can have as many elif tests as needed

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f'Your admission cost is ${price}.')

#Omitting the else block
#Sometimes it's clearer to use a final elif instead of else

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f'Your admission cost is ${price}.')

#Testing multiple conditions - use independent if statements
#All tests run, not just the first True one

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print('Adding mushrooms.')
if 'pepperoni' in requested_toppings:
    print('Adding pepperoni.')
if 'extra cheese' in requested_toppings:
    print('Adding extra cheese.')

print('\nFinished making your pizza!')

#if-elif-else only runs ONE block
#This would be WRONG for the pizza - it would miss toppings

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print('Adding mushrooms.')
elif 'pepperoni' in requested_toppings:
    print('Adding pepperoni.')
elif 'extra cheese' in requested_toppings:
    print('Adding extra cheese.')

print('\nFinished making your pizza!')

#TRY IT YOURSELF

#5-3 Alien Colors #1

alien_color = 'green'
if alien_color == 'green':
    print('+5 points for Player 1!')

alien_color = 'red'
if alien_color == 'green':
    print('+5 points for Player 1!')

#5-4 Alien Colors #2

alien_color = 'yellow'
if alien_color == 'green':
    print('+5 points for Player 1!')
else:
    print('+10 points for Player 1!')

alien_color = 'green'
if alien_color == 'green':
    print('+5 points for Player 1!')
else:
    print('+10 points for Player 1!')

#Print 5-5 Alien Colors #3

alien_color = 'green'
if alien_color == 'green':
    print('+5 points for Player 1!')
elif alien_color == 'yellow':
    print('+10 points for Player 1!')
else:
    print('+15 points for Player 1!')

alien_color = 'red'
if alien_color == 'green':
    print('+5 points for Player 1!')
elif alien_color == 'yellow':
    print('+10 points for Player 1!')
else:
    print('+15 points for Player 1!')

alien_color = 'yellow'
if alien_color == 'green':
    print('+5 points for Player 1!')
elif alien_color == 'yellow':
    print('+10 points for Player 1!')
else:
    print('+15 points for Player 1!')

#5-6 Stages of Life

age = 25
if age < 2:
    print('People under 2 are babies.')
elif age < 4:
    print('People between 2 and 4 are toddlers.')
elif age < 13:
    print('People between 4 and 13 are kids.')
elif age < 20:
    print('People between 13 and 20 are teenagers.')
elif age < 65:
    print('People between 20 and 65 are adults.')
elif age >= 65:
    print('People 65 and older are elders.')

#OR

age = 25
if age < 2:
    print('People under 2 are babies.')
elif age < 4:
    print('People between 2 and 4 are toddlers.')
elif age < 13:
    print('People between 4 and 13 are kids.')
elif age < 20:
    print('People between 13 and 20 are teenagers.')
elif age < 65:
    print('People between 20 and 65 are adults.')
else:
    print('People 65 and older are elders.')

#5-7 Favorite Fruits

favorite_fruits = ['pineapple', 'mangoes', 'apples']
if 'pineapple' in favorite_fruits:
    print('I really like pineapple!')
if 'bananas' in favorite_fruits:
    print('I really like bananas!')
if 'mangoes' in favorite_fruits:
    print('I really like mangoes!')
if 'strawberries' in favorite_fruits:
    print('I really like strawberries!')
if 'apples' in favorite_fruits:
    print('I really like apples!')