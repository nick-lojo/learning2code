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