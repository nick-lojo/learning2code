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

