# Chapter 7 Part 3: while Loops with Lists and Dictionaries (PCC, pg. 124-127)

# A while loop can move items from one list to another
# pop() removes the last item from a list and returns it

# Start with users that need to be verified
# and an empty list to hold confirmed users

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users
# Move each verified user into the list of confirmed users.

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# Display all confirmed users

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# Use a while loop to remove ALL instances of a value from a list
# remove() only deletes the first instance it finds, so loop until it's gone

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

# A while loop can collect user input and store it directly in a dictionary
# This lets you connect each response to a specific person

responses = {}

# Set a flag to indicate that polling is active

polling_active = True

while polling_active:
    # Prompt for the person's name and response
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to snowboard someday? ")

    # Store the responses in the dictionary
    responses[name] = response

    # Find out if anyone else is going to take the poll
    repeat = input('Would you like to let another person respond? (yes/no) ')
    if repeat == 'no':
        polling_active = False

# Polling is complete. Show the results.

print("\n––– Poll Results –––")
for name, response in responses.items():
    print(f"{name.title()} would like to ride {response.title()}")

# TRY IT YOURSELF

# 7-8. Deli: Make a list called sandwich_orders and fill it with the names of
# various sandwiches. Then make an empty list called finished_sandwiches. Loop
# through the list of sandwich orders and print a message for each order, such
# as I made your tuna sandwich. As each sandwich is made, move it to the list
# of finished sandwiches. After all the sandwiches have been made, print a
# message listing each sandwich that was made.

sandwich_orders = ['italian', 'pastrami', 'buffalo chicken', 'tuna melt']
finished_sandwiches = []

while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    print(f"Your {finished_sandwich.title()} is ready.")
    finished_sandwiches.append(finished_sandwich)

print('\nFinished Sandwiches:')
for finished_sandwich in finished_sandwiches:
    print(f"\t{finished_sandwich.title()}")

# 7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make
# sure the sandwich 'pastrami' appears in the list at least three times. Add
# code near the beginning of your program to print a message saying the deli
# has run out of pastrami, and then use a while loop to remove all occurrences
# of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
# in finished_sandwiches.

sandwich_orders = ['pastrami', 'italian', 'pastrami', 'buffalo chicken', 'tuna melt', 'pastrami']

print('\nSorry, the deli has run out of pastrami sandwiches.')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

finished_sandwiches = []
while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    print(f"\nYour {finished_sandwich.title()} is ready.")
    finished_sandwiches.append(finished_sandwich)

print(f'\nFinished Sandwiches: {len(finished_sandwiches)}')
for finished_sandwich in finished_sandwiches:
    print(f"\t{finished_sandwich.title()}")

# 7-10. Dream Vacation: Write a program that polls users about their dream
# vacation. Write a prompt similar to If you could visit one place in the
# world, where would you go? Include a block of code that prints the results
# of the poll.

responses = {}

polling_active = True

while polling_active:
    name = input("What is your name? ")
    response = input("Where would your dream vacation be? ")

    responses[name] = response

    repeat = input("Would you like to forward the poll (yes/no)? ")
    if repeat == 'no':
        polling_active = False

print('––Poll Results––')
for name, response in responses.items():
    print(f"{name.title()} would like to visit {response.title()}")