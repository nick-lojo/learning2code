# A scouting app loads a playbook file to display to the coaching
# staff. The file may or may not exist depending on whether the
# team has uploaded it yet.
#
# Your job: attempt to read a file called playbook.txt and print
# its contents. If the file doesn't exist, print a friendly
# message instead of crashing.

from pathlib import Path

path = Path('playbook.txt')

try:
    contents = path.read_text()
    print(contents)
except FileNotFoundError:
    print(f"Sorry, the file '{path}' does not exist.")

contents = "4-3 Defense"
contents += "\nCover 2 Zone"
contents += "\nPlay Action Pass"

path.write_text(contents)