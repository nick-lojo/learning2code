#Chapter 6, Part 2: Looping Through a Dictionary (PCC pg. 99-105)

#Looping through all key-value pairs with .items()
#Use two variables in the for loop - one for key, one for value

user_0 = {
    'username':'efermi',
    'first':'enrico',
    'last':'fermi'
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

#Using descriptive variable names instead of key/value
#Makes the code cleaner when you know what the data represents

favorite_language = {
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phil':'python'
}

for name, language in favorite_language.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

#Looping through all keys with .keys()
#Only need one variable - you're only getting keys

favorite_language = {
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phil':'python'
}

for name in favorite_language.keys():
    print(name.title())

#Looping through keys is the default behavior
#These two loops do the exact same thing:

for name in favorite_language.keys():
    print(name.title())

#Same as:

for name in favorite_language:
    print(name.title())

#Using keys to access values inside the loop
#Check if a key matches something, then grab its value

favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phil':'python'
}

friends = ['phil', 'sarah']

for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}")

#Checking if a key exists in the dictionary
#Use 'not in' with .keys() to see if someoen is missing

favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phil':'python'
}

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

#Looping through keys in sorted order with sorted()
#Wrap .keys() with sorted() to get alphabetical order

favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phil':'python'
}

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

#Looping through all values with .values()
#Only need one variable - you're only getting values

favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phil':'python'
}

print('The following languages have been mentioned:')
for language in favorite_languages.values():
    print(language.title())

#Using set() to get unique values only
#Wrap .values() with set() to remove duplicates

favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phil':'python'
}

print('The following languages have been mentioned:')
for language in set(favorite_languages.values()):
    print(language.title())

# TRY IT YOURSELF

# 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
# up the code from Exercise 6-3 (page 99) by replacing your series of print()
# calls with a loop that runs through the dictionary's keys and values. When
# you're sure that your loop works, add five more Python terms to your
# glossary. When you run your program again, these new words and meanings
# should automatically be included in the output.

glossary = {
    'list':'Where common values are stored',
    'loop':'Syntax that circles through a list',
    'print':'A function used to display text in the terminal',
    'if statement':'A conditional that triggers an outcome based on a specific input',
    'elif':'Allows the user to check multiple conditions and set unique outcomes to each one'
}

for term, definition in glossary.items():
    print(f"{term.title()}: {definition}\n")

#Add 5 more terms

glossary['dictionary'] = 'A function in Python used to correlate a key to a value'
glossary['key'] = 'The word defined by a value'
glossary['value'] = 'The definition of a key in a dictionary'
glossary['set()'] = 'A Python syntax used to filter the values in a dictionary without repeats'
glossary['sort()'] = 'A Python syntax used to filter dictionaries and lists alphabetically'

for term, definition in glossary.items():
    print(f"{term.title()}: {definition}\n")

# 6-5. Rivers: Make a dictionary containing three major rivers and the country
# each river runs through. One key-value pair might be 'nile': 'egypt'.
#   • Use a loop to print a sentence about each river, such as The Nile runs 
#     through Egypt.
#   • Use a loop to print the name of each river included in the dictionary.
#   • Use a loop to print the name of each country included in the dictionary.

rivers = {
    'nile':'egypt',
    'mississippi':'united states',
    'amazon':'brazil'
}

for river, country in rivers.items():
    print(f"The {river.title()} River runs through {country.title()}.\n")

for river in rivers.keys():
    print(f"{river.title()}\n")

for country in rivers.values():
    print(f"{country.title()}\n")

# 6-6. Polling: Use the code in favorite_languages.py (page 96).
#
#   • Make a list of people who should take the favorite languages poll.
#     Include some names that are already in the dictionary and some that are
#     not.
#   • Loop through the list of people who should take the poll. If they have
#     already taken the poll, print a message thanking them for responding.
#     If they have not yet taken the poll, print a message inviting them to
#     take the poll.

take_poll = ['phil', 'jen', 'bobby', 'janice']

favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phil':'python'
}

for name in take_poll:
    if name in favorite_languages:
        print(f'Thank you, {name.title()}, for taking our poll!')
    else:
        print(f'{name.title()}, could you please respond to our poll?')