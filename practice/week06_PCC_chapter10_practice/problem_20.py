# A library catalog system stores book titles in a file called
# catalog.txt, one title per line. A new feature needs to display
# each title individually to the screen.
#
# Your job: read the file and print each title on its own line.

from pathlib import Path

path = Path('catalog.txt')
contents = path.read_text()
lines = contents.splitlines()

for line in lines:
    print(line.strip())