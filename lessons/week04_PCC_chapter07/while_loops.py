# Chapter 7 Part 2: while Loops (PCC, pg. 117-123)

# A while loop keeps running as long as a condition is True
# This one counts from 1 to 5

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# You can let the user decide when to quite by checking for a quite value
# message starts as "" so the while condition has something to check on first
# run

prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

# A flag is a variable that controls whether the loop keeps running
# Useful when multiple events could stop the program

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

# break exits the loop immediately, no matter what the condition says
# while True runs forever until a break is hit

while True:
    city = input("\nPlease enter the name of a city that you have visited:"
                 "\n(Enter 'quit' when you are finished.) ")
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")

# THE PROBLEM: what prints when user types 'quit'?
#
# -------------------------------------------------------
# METHOD 1: while != (WITHOUT the if guard inside)
#
# message = ""
# while message != 'quit':
#     message = input("Enter a city: ")
#     print(f"I'd love to go to {message.title()}!")  # no guard!
#
# TERMINAL:
# Enter a city: Tokyo
# I'd love to go to Tokyo!
# Enter a city: quit
# I'd love to go to Quit!
# 
# # Issue: print runs before loop checks condition
#
# -------------------------------------------------------
# METHOD 2: active flag (WITHOUT the else block)
#
# active = True
# while active:
#     message = input("Enter a city: ")
#     if message == 'quit':
#         active = False
#     print(f"I'd love to go to {message.title()}!")
# 
# no else, runs regardless!
#
# TERMINAL:
# Enter a city: Tokyo
# I'd love to go to Tokyo!
# Enter a city: quit
# I'd love to go to Quit!
# 
# #Issue: print is outside the else, still runs
#
# -------------------------------------------------------
# METHOD 3: break (no guard needed, impossible to bug this way)
#
# while True:
#     city = input("Enter a city: ")
#     if city == 'quit':
#         break               # exits immediately, next line never reached
#     print(f"I'd love to go to {city.title()}!")
#
# TERMINAL:
# Enter a city: Tokyo
# I'd love to go to Tokyo!
# Enter a city: quit
# nothing prints, break fired before print
#
# -------------------------------------------------------
# BOTTOM LINE:
# !=     = needs if guard inside or it processes 'quit' like any other input
# active = needs else block or print runs even when active is set to False
# break  = structurally impossible to accidentally process 'quit'
#
# WHY 'quit' PRINTS BY ACCIDENT WITH != AND active
#
# The problem: print() is inside the loop, so it runs BEFORE
# the loop has a chance to check if it should stop.
#
# -------------------------------------------------------
# != WITHOUT a guard:
#
# while message != 'quit':
#     message = input("Enter a city: ")
#     print(f"I'd love to go to {message.title()}!")
#
# TERMINAL:
# Enter a city: quit
# I'd love to go to Quit!    # Issue: print ran before loop checked condition
#
# -------------------------------------------------------
# active WITHOUT an else block:
#
# while active:
#     message = input("Enter a city: ")
#     if message == 'quit':
#         active = False
#     print(f"I'd love to go to {message.title()}!")
#
# TERMINAL:
# Enter a city: quit
# I'd love to go to Quit!      # Issue: print is outside the if, runs anyway
#
# -------------------------------------------------------
# break NEEDS NO GUARD:
#
# while True:
#     city = input("Enter a city: ")
#     if city == 'quit':
#         break
#     print(f"I'd love to go to {city.title()}!")
#
# TERMINAL:
# Enter a city: quit
#                                   # break fires, print never reached
#
# -------------------------------------------------------
# BOTTOM LINE:
# != and active require you to manually guard against processing 'quit'
# break structurally prevents it — nothing below break ever runs
#
# != – one condition stops the loop, simple scripts
# active – multiple conditions can stop the loop, more complex programs
# break – stops immediately mid-loop, no accidental processing of the exit
#         value

# continue skips the rest of the loop and jumps back to the top
# This prints only odd numbers by skippiung even ones

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

# continue skips the rest of the current cycle and jumps back to the top
# break kills the loop entirely
# This prints only odd numbers by skipping even ones
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue        # even number? skip print, go back to top
    print(current_number)

# Avoiding Infinite Loops
# Every while loop needs a way to stop or it runs forever
# This loop would run forever without current_number += 1

x = 1
while x <= 5:
    print(x)
    x += 1 # Remove this line and it prints 1 forever

# If you get stuck in an infinite loop, press CTRL-C to force stop

# TRY IT YOURSELF
# 
# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
# pizza toppings until they enter a 'quit' value. As they enter each topping,
# print a message saying you'll add that topping to their pizza.

prompt = "Please enter your desired pizza toppings."
prompt += "\nPlease enter 'quit' when you are done. "

pizza_toppings = ""

while pizza_toppings != 'quit':
    pizza_toppings = input(prompt)
    if pizza_toppings != 'quit':
        print(f"{pizza_toppings.title()} added to your order.")

# 7-5. Movie Tickets: A movie theater charges different ticket prices
# depending on a person's age. If a person is under the age of 3, the ticket
# is free; if they are between 3 and 12, the ticket is $10; and if they are
# over age 12, the ticket is $15. Write a loop in which you ask users their
# age, and then tell them the cost of their movie ticket.

prompt = "Please enter your age so we can determine the price of your ticket."
prompt += "\nPlease enter 'quit' after entering all ages. "

active = True

while active:
    age = input(prompt)
    if age == 'quit':
        active = False
    else:
        age = int(age)
        if age < 3:
            print("Tickets are free for those under 3 years-old.")
        elif age <= 12:
            print(f"Tickets are $10 for those aged {age} years-old.")
        else:
            print('Tickets are $15 for those over 12 years-old.')

# 7-6. Three Exits: Write different versions of either Exercise 7-4 or 7-5
# that do each of the following at least once:
# - Use a conditional test in the while statement to stop the loop.
# - Use an active variable to control how long the loop runs.
# - Use a break statement to exit the loop when the user enters a 'quit'
#   value.

print("Start 7-6 Input")

# Conditional Test

prompt = "Please enter your desired pizza toppings."
prompt += "\nPlease enter 'quit' when you are done. "

pizza_toppings = ""

while pizza_toppings != 'quit':
    pizza_toppings = input(prompt)
    if pizza_toppings != 'quit':
        print(f"Adding {pizza_toppings.title()} to your pizza.")
print("\nYour pizza is ready!")

# Active Variable

prompt = "\nPlease enter your desired pizza toppings."
prompt += "\nPlease enter 'quit' when you are done. "

active = True
while active:
    pizza_toppings = input(prompt)
    if pizza_toppings == 'quit':
        print("\nYour pizza is ready!")
        active = False
    else:
        print(f"Adding {pizza_toppings} to the pizza!")

# Break

while True:
    pizza_toppings = input("\nPlease enter your desired pizza toppings."
                           "\nPlease enter 'quit' when you are done. ")
    if pizza_toppings == 'quit':
        print('\nYour pizza is ready!')
        break
    else:
        print(f"Adding {pizza_toppings.title()} to the pizza!")

# 7-7. Infinity: Write a loop that never ends, and run it. (To end the loop,
# press CTRL-C or close the window displaying the output.)

x = 1
while x < 100:
    print(x)