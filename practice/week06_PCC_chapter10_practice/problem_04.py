# You're building a lap time analyzer. A file called splits.txt
# contains several lap times, one per line.
# 
# Your job: print each line of the file individually using a loop.

from pathlib import Path

path = Path('splits.txt')
contents = path.read_text()
lines = contents.splitlines()

for line in lines:
    print(line)