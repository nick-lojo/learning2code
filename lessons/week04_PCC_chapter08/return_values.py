# Chapter 8 Part 3: Return Values (PCC, pg. 137-141)

# A function can process data and send a result back to the caller
# The return statement exits the function and sends the value back
# Assign the result to a variable to use it outside the function

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# An optional argument has a default of empty string so it can be ommitted
# Move optional parameters to the end of the definition
# Check if the optional value was provided using an if statement

def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

# A function can return any data type, including a dictionary
# This lets you package related data together and work with it after the call
# None is a placeholder value – in conditional tests it evaluates to False

def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first':first_name, 'last':last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)

# Functions work with any Python structure, including while loops
# Use break to give the user a way to exit the loop cleanly

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

# TIY

# 8-6. City Names: Write a function called city_country() that takes in the
# name of a city and its country. The function should return a string
# formatted like this: "Santiago, Chile"
# Call your function with at least three city-country pairs and print the
# values that are returned.

def city_country(city, country):
    """Neatly formats a city and the country it is in."""
    output = f"{city}, {country}"
    return output.title()

output_1 = city_country('madrid', 'spain')
print(output_1)

output_2 = city_country('sydney', 'austrailia')
print(output_2)

output_3 = city_country('tokyo', 'japan')
print(output_3)

# 8-7. Album: Write a function called make_album() that builds a dictionary
# describing a music album. The function should take in an artist name and
# an album title and return a dictionary containing these two pieces of
# information. Use None to add an optional parameter for the number of songs.
# If included, add it to the dictionary. Make three dictionaries and print each.

def make_album(artist_name, album_title, number_songs=None):
    """Builds a dictionary describing a music album."""
    album = {'artist name':artist_name.title(), 'album_title':album_title.title()}
    if number_songs:
        album['number songs'] = number_songs
    return album

album_1 = make_album('jimi hendrix', 'axis: bold as love', number_songs=13)
print(album_1)

album_2 = make_album('sabrina carpenter', "man's best friend")
print(album_2)

album_3 = make_album(album_title='american idiot', artist_name='green day')
print(album_3)

# 8-8. User Albums: Start with 8-7. Write a while loop that allows users to
# enter an album's artist and title. Call make_album() with the user's input
# and print the dictionary that's created. Include a quit value in the loop.

def make_album(artist_name, album_title):
    """Builds a dictionary describing a music album."""
    album = {'artist name':artist_name.title(), 'album_title':album_title.title()}
    return album

while True:
    print("\nPlease enter the artist's name and the album.")
    print("Enter 'q' at any time to stop.")
    a_name = input("\nPlease enter the artist's name: ")
    if a_name == 'q':
        break
    a_title = input("\nPlease enter the album title: ")
    if a_title == 'q':
        break
    album = make_album(a_name, a_title)
    print(f"\nAlbum: {album}")