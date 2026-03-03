# Chapter 8 Part 4: Passing a List (PCC, pg. 142-145)

# You can pass a list to a function just like any other argument
# The function gets direct access to the list's contents

def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# Changes made to a list inside a function are permanent
# This lets you reorganize data efficiently across two lists

def print_models(unprinted_desgins, completed_models):
    """Simulate printing each design until none are left."""
    while unprinted_desgins:
        current_design = unprinted_desgins.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# Passing a copy of a list protects the original from being modified
# Slice notation [:] creates a copy – the function works on the copy only

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print(f"\nOriginal list still intact: {unprinted_designs}")

# TIY

# 8-9. Messages: Make a list containing a series of short text messages.
# Pass the list to a function called show_messages() that prints each message.

messages = ['hi', 'lol', 'omg', 'brb', 'ttyl']

def show_messages(messages):
    """Prints messages in a list."""
    for message in messages:
        print(message)

show_messages(messages)

# 8-10. Sending Messages: Write a function called send_messages() that prints
# each message and moves it to a new list called sent_messages as it's printed.
# After calling the function, print both lists to confirm messages were moved.

def send_messages(messages, sent_messages):
    """Prints messages as they send, then moves them to a new list."""
    while messages:
        send_message = messages.pop()
        print(f'Message Sent: "{send_message}"')
        sent_messages.append(send_message)

def show_messages(sent_messages):
    """Shows messages that were sent."""
    print(f"\nThe following messages have been sent:")
    for message in sent_messages:
        print(f"{message}")

messages = ['hi', 'lol', 'omg', 'brb', 'ttyl']
sent_messages = []

send_messages(messages, sent_messages)
show_messages(sent_messages)

# 8-11. Archived Messages: Call send_messages() with a copy of the messages
# list. After calling the function, print both lists to show the original
# list has retained its messages.

messages = ['hi', 'lol', 'omg', 'brb', 'ttyl']
sent_messages = []

send_messages(messages[:], sent_messages)
show_messages(sent_messages)

print(messages)
print(sent_messages)