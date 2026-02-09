#Chapter 6 Part 1: Working with Dictionaries (PCC, pg. 92-99)

#A simple dictionary – stores key-value pairs
#The alien's color and point value are connected

alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

#Dictionary syntax: braces with key-value pairs
#Key and value separated by colon, pairs separated by commas

alien_0 = {'color': 'green', 'points': 5}

#Accessing values - use the key in square brackets
#Give dictionary name, then [key] to get the value

alien_0 = {'color': 'green'}
print(alien_0['color'])

#Using the accesssed value in your code
#Pull the value, store it in avariable, use it

alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print(f'You just earned {new_points} points!')

#Adding new key-value pairs
#Assign a value to a new key using square brackets

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#Starting with an empty dictionary
#Define with empty braces, then add pairs one by one

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

#Modifying values in a dictionary
#Assign a new value to an existing value

alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is {alien_0['color']}.")

#Using dictionary values to control behavior
#Read a value, make a decision, modify another value

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

#Determine how far to move based on current speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

#Update position
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

#Removing key-value pairs with del
#Use del statement with dictionary name and key

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

#A dictionary of similar objects
#Store the same kind of information about different items

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

#Using get() for safe access
#If the key doesn't exist, square brackets cause an error
#get() return a default value instead

alien_0 = {'color':'green', 'speed':'slow'}

#This would crash: print(alien_0['points'])
#Use get() instead:

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

# TRY IT YOURSELF

# 6-1. Person: Use a dictionary to store information about a person
# you know. Store their first name, last name, age, and the city in
# which they live. You should have keys such as first_name, last_name,
# age, and city. Print each piece of information stored in your
# dictionary. Please note I will use a fictional character since I
#am publishing this file to github.

person_1 = {}
person_1['first_name'] = 'Walter'
person_1['last_name'] = 'White'
person_1['age'] = 51
person_1['city'] = 'Albuquerque'

print(person_1['first_name'])
print(person_1['last_name'])
print(person_1['age'])
print(person_1['city'])
print(person_1)

# 6-2. Favorite Numbers: Use a dictionary to store people's favorite
# numbers. Think of five names, and use them as keys in your
# dictionary. Think of a favorite number for each person, and store
# each as a value in your dictionary. Print each person's name and
# their favorite number. For even more fun, poll a few friends and get
# some actual data for your program.

favorite_numbers = {
    'Tom':12,
    'Rob':87,
    'Drake':10,
    'Marty':26,
    'Kylian':9
}

print(f"Tom's favorite number is {favorite_numbers['Tom']}.")
print(f"Rob's favorite number is {favorite_numbers['Rob']}.")
print(f"Drake's favorite number is {favorite_numbers['Drake']}.")
print(f"Marty's favorite number is {favorite_numbers['Marty']}.")
print(f"Kylian's favorite number is {favorite_numbers['Kylian']}.")

# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let's call it a glossary.
# 
# • Think of five programming words you've learned about in the
#   previous chapters. Use these words as the keys in your glossary,
#   and store their meanings as values.
# 
# • Print each word and its meaning as neatly formatted output. You
#   might print the word followed by a colon and then its meaning, or
#   print the word on one line and then print its meaning indented
#   on a second line. Use the newline character (\n) to insert a blank
#   line between each word-meaning pair in your output.

glossary = {
    'list':'Where common values are stored',
    'loop':'Syntax that circles through a list',
    'print':'A function used to display text in the terminal',
    'if statement':'A conditional that triggers an outcome based on a specific input',
    'elif':'Allows the user to check multiple conditions and set unique outcomes to each one'
}

print(f"List: {glossary['list']}\n")
print(f"Loop: {glossary['loop']}\n")
print(f"Print: {glossary['print']}\n")
print(f"If Statement: {glossary['if statement']}\n")
print(f"elif: {glossary['elif']}")