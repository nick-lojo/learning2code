# Chapter 10 Part 3: Exceptions (PCC, pg. 192-200)

# Exceptions (PCC, pg. 192)

# Python creates exception objets when it encounters an error it can't handle.
# If unhandled, the program halts and shows a traceback.
# try-except blocks let us handle excpetions gracefully instead of crashing.

# Handling the ZeroDivisionError

try:
    print(5/0) # this line will riase a ZeroDivisionError
except ZeroDivisionError:
    print("You can't divide by zero!")

# Using Exceptions to Prevent Crashes (PCC, pg. 193-194)
# Without exception handling, bad input crashes the program entirely.
# Wrapping risk code in try-except keeps the program running.

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)

# The else Block (PCC, pg. 194-195)
# Code in the else block runs ONLY if the try block succeeded.
# try = risky code. except = handle the error. else = run if no error occurred.

# Handling the FileNotFoundError Exception (PCC, pg. 195-196)
# A common error when owkring with files -- the file doesn't exist.
# The traceback tells us exactly which exception to catch.

from pathlib import Path

path = Path('alice.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")

# Analyzing Text (PCC, pg. 196-197)
# Once a file is read into memory, we can run any string operations on it.
# split() breaks a string into a list of words wherever it finds whitespace.

path = Path('alice.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
else:
    words = contents.split() # splits the string into a list of words
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")

# Working with Multiple Files (PCC, pg. 197-198)
# We can loop over a list of filenames and run the same logic on each.
# Files that are missing don't stop the prorgam -- the exception is caught per file

def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    path = Path(filename)
    count_words(path)

# Failing Silently (PCC, pg. 198-199)
# Sometimes you don't want to report errors to the user at all.
# The pass statement tells Python to do nothing in the except block

def count_words_silent(path):
    """Count the approximate number of words in a file, fail silently."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass # do nothing -- user doesn't need to know the file is missing
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

for filename in filenames:
    path = Path(filename)
    count_words_silent(path)

# Deciding Which Errors to Report (PCC, pg. 199)
# Not every exception needs to be reported to the user.
# Report errors when users need the information to understand the missing results.
# Fail silently when the error is irrelevent to the user's experience.
# Well-written code handles external dependencies (files, input, network)
# with exception handling -- these are the most common sources of runtime errors.

# Try It Yourself

# 10-6. Addition: One common problem when prompting for numerical input occurs
# when people provide text instead of numbers. When you try to convert the input
# to an int, you'll get a ValueError. Write a program that prompts for two
# numbers. Add them together and print the result. Catch the ValueError if
# either input value is not a number, and print a friendly error message. Test
# your program by entering two numbers and then by entering some text instead
# of a number.

print("\nProvide me with two numbers, and I will add them for you!")
print("Enter 'q' to quit at any time.")

while True:
    first_number = input("\nPlease provide the first number: ")
    if first_number == 'q':
        break
    
    second_number = input("Please provide your second number: ")
    if second_number == 'q':
        break
    
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("\nYou can only add numbers!")
    else:
        print(answer)

# 10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop
# so the user can continue entering numbers, even if they make a mistake and
# enter text instead of a number.

# See 10-6

# 10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least
# three names of cats in the first file and three names of dogs in the second
# file. Write a program that tries to read these files and print the contents
# of the file to the screen. Wrap your code in a try-except block to catch the
# FileNotFound error, and print a friendly message if a file is missing. Move
# one of the files to a different location on your system, and make sure the
# code in the except block executes properly.

cats = Path('cats.txt')
cats_contents = 'georgie\n'
cats_contents += 'gracie\n'
cats_contents += 'inkie'
cats.write_text(cats_contents.title())

dogs = Path('dogs.txt')
dogs_contents = 'henry\n'
dogs_contents += 'archie\n'
dogs_contents += 'royce'
dogs.write_text(dogs_contents.title())

def read_names(path):
    """Reads names in a file and prints them."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f'\nSorry, {path} does not exist in this library.')
    else:
        print(f"\n{contents}")

animal_names = ['dogs.txt', 'cats.txt', 'birds.txt']
for file in animal_names:
    path = Path(file)
    read_names(path)

# 10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-8 to
# fail silently if either file is missing.