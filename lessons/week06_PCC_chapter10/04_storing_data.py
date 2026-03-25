# Chapter 10 Part 4: Storing Data (PCC, pg. 201-206)

# Storing Data with JSON (PCC, pg. 201)
# The json module lets us convert Python data structures into JSON format.
# JSON is language-agnostic -- it can be shared between Python, JavaScript, etc.
# json.dumps() convets Python data TO a JSON string.
# json.loads() converts a JSON string BACK to Python data.

from pathlib import Path
import json

# json.dumps() -- Writing Data to JSON (PCC, pg. 201-202)

numbers = [2, 3, 5, 7, 11, 13]
path = Path('numbers.json')
contents = json.dumps(numbers) # converts the list to a JSON-formatted string
path.write_text(contents)

# json.loads() -- Reading Data from JSON (PCC, pg. 202)

path = Path('numbers.json')
contents = path.read_text()
numbers = json.loads(contents) # converts the JSON string back to a Python list
print(numbers)

# Saving and Reading User-Generate Data (PCC, pg. 202-203)
# json is useful for persisting user data between program runs.
# Without saving it, data is lost the moment the program stops.

path = Path('username.json')
username = input('What is your name? ')
contents = json.dumps(username)
path.write_text(contents)
print(f"We'll remember you when you come back, {username}!")

# Reading back user-generated data (PCC, pg. 203)

path = Path('username.json')
contents = path.read_text()
username = json.loads(contents)

print(f"Welcome back, {username}!")

# path.exists() -- Checking if a File Exisits (PCC, pg. 203)
# Instead of try-except, we can check if a file exists before reading it.
# path.exists() returns True if the file exsts, False if it doesn't.

path = Path('username.json')
if path.exists():
    contents = path.read_text()
    username = json.loads(contents)
    print(f"Welcome back, {username}!")
else:
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    print(f"We'll remember you when you come back, {username}")

# Refactoring (PCC, pg. 204-206)
# Refactoring = restructuring exisitng code without changing what it does.
# Goal: cleaner, more readable, easier to extend.
# Each function should have ONE clear job.

def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None # explicity None returned when no username found

def get_new_username(path):
    """Prompt for a new username and store it."""
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")

greet_user()

# Try It Yourself

# 10-11. Favorite Number: Write a program that prompts for the user's favorite
# number. Use json.dumps() to store this number in a file. Write a separate
# program that reads in this value and prints the message
# "I know your favorite number! It's _____."

favorite_number = input("What is your favorite number? ")
path = Path('favorite_number.json')
contents = json.dumps(favorite_number)
path.write_text(contents)

path = Path('favorite_number.json')
contents = path.read_text()
number = json.loads(contents)
print(f"I know your favorite number! It's {number}.")

# 10-12. Favorite Number Remembered: Combine the two programs you wrote in
# Exercise 10-11 into one file. If the number is already stored, report the
# favorite number to the user. If not, prompt for the user's favorite number
# and store it in a file. Run the program twice to see that it works.

path = Path('favorite_number.json')

if path.exists():
    contents = path.read_text()
    number = json.loads(contents)
    print(f"I know your favorite number! It's {number}.")
else:
    favorite_number = input("What is your favorite number? ")
    contents = json.dumps(favorite_number)
    path.write_text(contents)

# 10-13. User Dictionary: The remember_me.py example only stores one piece of
# information, the username. Expand this example by asking for two more pieces
# of information about the user, then store all the information you collect in
# a dictionary. Write this dictionary to a file using json.dumps(), and read it
# back in using json.loads(). Print a summary showing exactly what your program
# remembers about the user.

def greet_user():
    """Greet the user by name."""
    path = Path('user_info.json')
    if path.exists():
        contents = path.read_text()
        user_info = json.loads(contents)
        print(f"Welcome back, {user_info['user_info']['username']}")
    else:
        username = input('What is your username? ')
        name = input('What is your name? ')
        email = input('What is your email? ')
        user = {}
        user['user_info'] = {
            'username':username,
            'name':name.title(),
            'email':email
        }
        contents = json.dumps(user)
        path.write_text(contents)
        print(f"We'll remember you when you comeback, {user['user_info']['username']}")

greet_user()

# 10-14. Verify User: The final listing for remember_me.py assumes either that
# the user has already entered their username or that the program is running for
# the first time. We should modify it in case the current user is not the person
# who last used the program. Before printing a welcome back message in
# greet_user(), ask the user if this is the correct username. If it's not, call
# get_new_username() to get the correct username.

def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None # explicity None returned when no username found

def get_new_username(path):
    """Prompt for a new username and store it."""
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        question = input(f"Is this your username: {username}? (yes / no)? ")
        if question == 'yes':
            print(f"Welcome back, {username}!")
        elif question == 'no':
            username = get_new_username(path)
            print(f"We'll remember you when you come back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")

greet_user()