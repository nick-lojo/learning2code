#Chapter 6 Part 3: Nesting (PCC pg. 105-112)

#A list of dictionaries
#Store multiple dictionaries in a list

alien_0 = {'color':'green', 'points':5}
alien_1 = {'color':'yellow', 'points':10}
alien_2 = {'color':'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

#Making 30 aliens automatically with a loop
#Each alien is a dictionary added to the list

aliens = []

for alien_number in range(30):
    new_alien = {'color':'green', 'points':5, 'speed':'slow'}
    aliens.append(new_alien)

#Show the first 5 aliens

for alien in aliens[:5]:
    print(alien)
print('...')

#Show how many aliens have been created

print(f"Total number of aliens {len(aliens)}")

#Changing the first 3 aliens to yellow, medium-speed aliens

aliens = []

for alien_number in range(30):
    new_alien = {'color':'green', 'points':5, 'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

#Show the first 5 aliens

for alien in aliens [:5]:
    print(alien)
print('...')

#A list in a dictionary
#Store a list in a dictionary

pizza = {
    'crust':'thick',
    'toppings':['mushrooms', 'extra cheese']
}

print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")

#Lists as values - people can have multiple favorites

favorite_languages = {
    'jen':['python', 'rust'],
    'sarah':'c',
    'edward':['rust', 'go'],
    'phil':['python', 'haskell']
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

#Checking length to use correct grammar

favorite_languages = {
    'jen':['python', 'rust'],
    'sarah':['c'],
    'edward':['rust', 'go'],
    'phil':['python','haskell']
}

for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print(f"\n{name.title()}'s favorite languages are:")
    elif len(languages) == 1:
        print(f"\n{name.title()}'s favorite language is:")
    else:
        print(f"\n{name.title()} does not have a favorite language.")
    for language in languages:
        print(f"\t{language.title()}")

#A dictionary in a dictionary
#Each user's info is stored as a dictionary

users = {
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton',
    },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

# TRY IT YOURSELF

# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 98).
# Make two new dictionaries representing different people, and store all
# three dictionaries in a list called people. Loop through your list of people.
# As you loop through the list, print everything you know about each person.

person_1 = {} #From 6-1
person_1['first_name'] = 'Walter'
person_1['last_name'] = 'White'
person_1['age'] = 51
person_1['city'] = 'Albuquerque'

person_2 = {
    'first_name':'Jesse',
    'last_name': 'Pinkman',
    'age':26,
    'city':'Albuquerque',
}

person_3 = {
    'first_name':'Gustavo',
    'last_name':'Fring',
    'age':'Dead',
    'city':'Albuquerque'
}

people = [person_1, person_2, person_3]

for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    print(f"\nName: {full_name}")
    print(f"\tAge: {person['age']}")
    print(f"\tLocation: {person['city']}")

# 6-8. Pets: Make several dictionaries, where each dictionary represents a
# different pet. In each dictionary, include the kind of animal and the owner's
# name. Store these dictionaries in a list called pets. Next, loop through
# your list and as you do, print everything you know about each pet.

pet_0 = {
    'name':'henry',
    'species':'dog',
    'breed':'corgi',
    'color':'tricolor',
    'age':2,
    'parent':'pumpkin',
}

pet_1 = {
    'name':'archie',
    'species':'dog',
    'breed':'corgi',
    'color':'tricolor',
    'age':1,
    'parent':'daisy',
}

pet_2 = {
    'name':'royce',
    'species':'dog',
    'breed':'pug',
    'color':'fawn',
    'age':'deceased',
    'parent':'unknown'
}

pet_3 = {
    'name':'georgie',
    'species':'cat',
    'breed':'unknown',
    'color':'black',
    'age':'deceased',
    'parent':'unknown',
}

pets = [pet_0, pet_1, pet_2, pet_3]

for pet in pets:
    name = f"{pet['name']}"
    print(f"\nName: {name.title()}")

    species = f"{pet['species']}"
    print(f"\tSpecies: {species.title()}")

    breed = f"{pet['breed']}"
    print(f"\tBreed: {breed.title()}")

    color = f"{pet['color']}"
    print(f"\tColor: {color.title()}")

    age = f"{pet['age']}"
    print(f"\tAge: {age.title()}")

    parent = f"{pet['parent']}"
    print(f"\tParent: {parent.title()}")

# 6-9. Favorite Places: Make a dictionary called favorite_places. Think of
# three names to use as keys in the dictionary, and store one to three
# favorite places for each person. To make this exercise a bit more
# interesting, ask some friends to name a few of their favorite places. Loop
# through the dictionary, and print each person's name and their favorite
# places.

favorite_places = {
    'henry':['japan','spain','australia'],
    'archie':['spain', 'hungary', 'czechia'],
    'mike':['italy', 'japan']
}

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")

# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 98) so
# each person can have more than one favorite number. Then print each person's
# name along with their favorite numbers.

favorite_numbers = {
    'Tom':[12,10],
    'Rob':[87,48],
    'Drake':[10,12],
    'Marty':[26,8],
    'Kylian':[9,7,10]
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name}' favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")

# 6-11. Cities: Make a dictionary called cities. Use the names of three cities
# as keys in your dictionary. Create a dictionary of information about each
# city and include the country that the city is in, its approximate population,
# and one fact about that city. The keys for each city's dictionary should be
# something like country, population, and fact. Print the name of each city
# and all of the information you have stored about it.

cities = {
    'tokyo':{
        'country':'japan',
        'population':40000000,
        'fact':'This is the most populous metro area in the world!',
    },
    'madrid':{
        'country':'spain',
        'population':3500000,
        'fact':"Madrid is home to the world's oldest restaurant, El Botin!",
    },
    'sydney':{
        'country':'australia',
        'population':5500000,
        'fact':'You can see kangaroos in Sydney!',
    }
}

for city, info in cities.items():
    print(f"\n{city.title()}:")
    country = f"{info['country']}"
    population = f"{info['population']}"
    fact = f"{info['fact']}"
    print(f"\tCountry: {country.title()}")
    print(f"\tPopulation: {population}")
    print(f"\t{fact}")