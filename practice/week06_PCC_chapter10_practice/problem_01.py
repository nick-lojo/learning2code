# You're building a race results viewer for a local karting event.
# A file called lap_times.txt exists in the same directory as your
# script. It contains a few lines of lap time data.
#
# Your job: get the entire contents of that file into your program
# and print them to the screen.

from pathlib import Path

path = Path('lap_times.txt')
contents = path.read_text(encoding='utf-8')
print(contents)