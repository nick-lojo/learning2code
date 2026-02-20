# Chapter 7 Part 1: User Input (PCC, pg. 113-117)

# input() pauses the program and waits for the user to type something
# Whatever they type gets stored in a variable

message = input('Tell me something, and I will report it back to you:')
print(message)

# A clear prompt tells the user exactly what to enter
# Always add a space after the color so their response isn't crammed against
# the prompt

name = input('Please enter your name: ')
print(f"\nHello, {name}!")

# For longer prompts, build the message across multiple lines using +=
# This keeps your input() call clean and readable

prompt = 'If you share your name, we can personalize the messages you see'
prompt += '\nWhat is your first name? '
name = input(prompt)
print(f"\nHello, {name}!")

# input() always returns a string, even if the user types a number
# int() converts that string to an integer so you can do math with it

height = input('How tall are you, in inches? ')
height = int(height)
if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

# The modulo operator (%) returns the remainder after division
# If the remainder is 0, the number divides evenly

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")

# 7-1. Rental Car: Write a program that asks the user what kind of rental
# car they would like. Print a message about that car, such as "Let me see if
# I can find you a Subaru."

rental_car = input("What rental car are you interested in? ")
print(f"\nLet me see if I can find you a {rental_car.title()}.")

# 7-2. Restaurant Seating: Write a program that asks the user how many people
# are in their dinner group. If the answer is more than eight, print a message
# saying they'll have to wait for a table. Otherwise, report that their table
# is ready.

party_size = input('How many people are in your party? ')
party_size = int(party_size)

if party_size < 9:
    print('\nYour table is ready!')
else:
    print('\nGive us a moment while we prepare a table for you.')

# 7-3. Multiples of Ten: Ask the user for a number, and then report whether
# the number is a multiple of 10 or not.

prompt = 'Give me a number and I will tell you if it is a multiple of 10 or'
prompt += ' not: '

number = input(prompt)
number = int(number)

if number % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")