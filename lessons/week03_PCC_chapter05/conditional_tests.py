#Simple example - printing car names with special handling for 'bmw'
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#Conditional tests - checking for equality
#The == operator returns True if values match, False if they don't

car = 'bmw'
print(car == 'bmw') #True - values match

car = 'audi'
print(car == 'bmw') #False- values don't match

#Testing for equality is case sensitive
car = 'Audi'
print(car == 'audi') #False - different capitalization

#Use .lower() to compare without caring about case
print(car.lower() == 'audi') #True - both lowercase now

#The original variable is unchanged
print(car) #Still 'Audi'

#Checking for inequality with !=
#Returns True if values are NOT equal

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

#Testing if numbers are not equal
answer = 17
if answer != 42:
    print('That is not the correct answer. Please try again!')

#Numerical comparisons
age = 18
print(age == 18) #Equal to

age = 19
print(age < 21) #Less than
print(age <= 21) #Less than or equal to
print(age > 21) #Greater than
print(age >= 21) #Greater than or equal to

#Using 'and to check multiple conditions
#BOTH conditions must be True for the overall test to pass

age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21) #False - second test fails

age_1 = 22
print(age_0 >= 21 and age_1 >= 21) #True - both tests pass

#Using 'or' to check multiple conditions
#At least ONE condition must be True for the test to pass

age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21) #True - first test passes

age_0 = 18
print(age_0 >= 21 or age_1 >= 21) #False - both tests fail

#Checking if a value is in a list
#Use the 'in' keyword

requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings) #True
print('pepperoni' in requested_toppings) #False

#Checking if a value is NOT in a list
#Use 'not in' keyword

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f'{user.title()}, you can post a response if you wish.')

#Boolean expressions - another name for conditional tests
#Boolean values are either True or False

game_active = True
can_edit = False

print(game_active)
print(can_edit)

#TRY IT YOURSELF

#5-1 Conditional Tests

#Example
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

#Created by me
patriots_qb = 'Drake Maye'
print("\nIs the Patriot's QB Drake Maye? I predict True.")
print(patriots_qb == 'Drake Maye')

print("\nIs the Patriot's QB Justin Fields? I predict False.")
print(patriots_qb == 'Justin Fields')

fav_drink = 'coffee'
print('\nIs my favorite drink coffee? I predict True.')
print(fav_drink == 'coffee')

print('\nIs my favorite drink soda? I predict False.')
print(fav_drink == 'soda')

commute = 'long'
print('\n Is my commute long? I predict True.')
print(commute == 'long')

print('\nIs my commute short? I predict False.')
print(commute == 'short')

car = 'EV'
print('\nDo I drive a EV? I predict True.')
print(car == 'EV')

print('\nDo I drive a gas car? I predict False.')
print(car == 'gas car')

hobby = 'snowboarding'
print('\nIs snowboarding one of my hobbies? I predict True.')
print(hobby == 'snowboarding')

print('\n Is knitting one of my hobbies? I predict False.')
print(hobby == 'knitting')

#5-2 More Conditional Tests

#Equality and inequality with strings
dog = 'corgi'
print('\nMy dog is a corgi.')
print(dog == 'corgi')

if dog != 'pug':
    print('\nMy dog is not a pug.')

#Tests using the lower.method
fav_food = 'Sushi'
print('\nMy favorite food is sushi.')
print(fav_food.lower() == 'sushi')

#Numerical tests involving equality, inequality,
#greater than and less than, greater than or equal to, and
#less than or equal to

number = 87

print('\nThe number is 87.')
print(number == 87)

answer = 78
if answer != 87:
    print('\nThe number is not 87.')

print('\nThe number is > 100.')
print(number > 100)

print('\nThe number is < 100.')
print(number < 100)

print('\nThe number is <= 78.')
print(number <= 78)

print('\nThe number is >= 78.')
print(number >= 78)

#Tests using 'and' and 'or'
print('\n87 is >= 50 and >= 100.')
print(number >= 50 and number >= 100)

print('\n87 is >= 50 or >= 100.')
print(number >= 50 or number >= 100)

#Test item in list
desserts = ['cookies', 'ice cream', 'cake']
print('\nIce cream is a dessert.')
print('ice cream' in desserts)

#Test item not in list
food = 'pizza'
if food not in desserts:
    print(f'\n{food.title()} is not a dessert.')