# Same race results file. When you print the contents, there's an
# extra blank line at the bottom of the output.
#
# Your job: print the contents without that trailing blank line.
# Do it in a single line of code where you read the file.

from pathlib import Path

path = Path('lap_times.txt')
contents = path.read_text()
print(contents.rstrip())