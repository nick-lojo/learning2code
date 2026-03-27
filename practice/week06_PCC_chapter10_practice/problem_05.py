# A weather station logs daily high temps in a file called temps.txt,
# one temperature per line. Some lines have leading spaces.
#
# Your job: read all the lines and build a single string containing
# all the temperatures with no extra whitespace. Print the result.

from pathlib import Path

path = Path('temps.txt')
contents = path.read_text()
lines = contents.splitlines()
temp_string = ''
for line in lines:
    temp_string += line.lstrip()
print(temp_string)