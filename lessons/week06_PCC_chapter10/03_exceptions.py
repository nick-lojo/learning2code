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