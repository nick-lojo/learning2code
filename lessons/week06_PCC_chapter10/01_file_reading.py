# Chapter 10 Part 1: Reading from a File (PCC, pg. 184-187)

# Reading the Contents of a File (pg. 184-185)
# The Path class from pathlib lets us point to a file on the system.
# read_txt() reads teh entire file and returns it as a single string.

from pathlib import Path

path = Path('pi_digits.txt') # creates a Path object pointing to the file
contents = path.read_text() # reads the file; returns contents as a string
print(contents)

# rstrip() removes trailing whitespace (including that extra blank line).
# Method chaininig applies rstrip() directly to the result of read_text().

contents = path.read_text().rstrip()
print(contents)

# Relative and Absolute File Paths (PCC, pg. 186)
# Relative path: Python looks relative to where the program is running from.
# Absolute path: tells Python the exact location on the system, starting from root.

# Relative Path Example (files is in subfolder called_text files)
# path = Path('text_files.pidigits.txt') # Have to ommit because no folder exists

# Absolute Path Example (full path from system root)
path = Path('/workspaces/learning2code/lessons/week06_PCC_chapter10/pi_digits.txt')

# Accessing a File's Lines (PCC, pg. 187)
# splitlines() turns the full file string into a list of individual lines.
# We can then loop over that list to work with each line one at a time.

contents = path.read_text()
lines = contents.splitlines() # return a list of lines, no newline characters
for line in lines:
    print(line)

# Working with a File's Contents (PCC, pg. 187-188)
# After reading lines into a list, we can build a single string from them.
# lstrip() removes the whitespace from the LEFT side of each line.

contents = path.read_text()
lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip() # strips leading spaces before concatenating
print(pi_string)
print(len(pi_string))

# Large Files: One Million Digits (PCC, pg. 188-189)
# The same code works on files of any size -- Python has no inherent data limit.
# We can use slicing to print only part of a large string.

# Example: if we had a million-digit pi file, we'd print just the first 52
# characters:

path = Path('pi_million_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

print(f"{pi_string[:52]}...")
print(len(pi_string))

# Is Your Birthday Contained in Pi? (PCC, pg. 189)
# Since pi_string is just a string, we can use 'in' to search it.

birthday = input('Enter your birtday, in the form mmddyy: ')
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")

# Try It Yourself

# 10-1. Learning Python: Open a blank file in your text editor and write a few
# lines summarizing what you've learned about Python so far. Start each line
# with the phrase In Python you can. . . . Save the file as learning_python.txt
# in the same directory as your exercises from this chapter. Write a program
# that reads the file and prints what you wrote two times: print the contents
# once by reading in the entire file, and once by storing the lines in a list
# and then looping over each line.

python_path = Path('learning_python.txt')
contents = python_path.read_text()
print(contents)

lines = contents.splitlines()
for line in lines:
    print(line)

# 10-2. Learning C: You can use the replace() method to replace any word in a
# string with a different word. Read in each line from the file you just
# created, learning_python.txt, and replace the word Python with the name of
# another language, such as C. Print each modified line to the screen.

for line in lines:
    print(line.replace('Python', 'C'))

# 10-3. Simpler Code: The program file_reader.py in this section uses a
# temporary variable, lines, to show how splitlines() works. You can skip
# the temporary variable and loop directly over the list that splitlines()
# returns. Remove the temporary variable from the splitlines() loop earlier
# in this file, to make it more concise.

path = Path('/workspaces/learning2code/lessons/week06_PCC_chapter10/pi_digits.txt')

contents = path.read_text()
for line in contents.splitlines():
    print(line)