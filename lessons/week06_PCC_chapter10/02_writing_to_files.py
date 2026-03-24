# Chapter 10 Part 2: Writing to a File (PCC, pg. 190-191)

from pathlib import Path

path = Path('programming.txt')
path.write_text('I love programming.')

# Writing Multiple Lines (PCC, pg. 191)
# To write multiple lines, build a single string first using +=
# Include \n at the end of each line so they appear on separate lines in the file.

contents = 'I love programming.\n'
contents += 'I love creating new games.\n'
contents += 'I also love working with data.\n'

path.write_text(contents)

# Try It Yourself

# 10-4. Guest: Write a program that prompts the user for their name. When they
# respond, write their name to a file called guest.txt.

name = input('Please state you name: ')
file = Path('guest_name.txt')
file.write_text(name)

# 10-5. Guest Book: Write a while loop that prompts users for their name.
# Collect all the names that are entered, and then write these names to a file
# called guest_book.txt. Make sure each entry appears on a new line in the file.

active = True
guest_book_names = ''

while active:
    message = f"Please enter your name to record in the Guest Book.\n"
    message += f"If all guests have entered their name, enter 'q': "
    name = input(message)
    if name == 'q':
        active = False
    else:
        guest_book_names += f"{name.title()}\n"
        guest_book = Path('guest_book.txt')
        guest_book.write_text(guest_book_names)