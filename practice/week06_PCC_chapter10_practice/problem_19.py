# A film studio tracks movie budgets in a file called budgets.txt.
# Each budget is on its own line. The studio needs a tool that
# builds a single combined string of all budgets with no newlines.
#
# Your job: read the file, process each line, and print one
# combined string with no extra whitespace.

from pathlib import Path

path = Path('budgets.txt')
contents = path.read_text()
lines = contents.splitlines()
budgets = ''
for line in lines:
    budgets += line
print(budgets)