# A parking garage system checks if a vehicle file exists before
# attempting to read it. If the file is missing, it should print
# a friendly message without crashing.
#
# Your job: attempt to read a file called vehicles.txt and print
# its contents. Handle the case where the file is missing.

from pathlib import Path

path = Path('vehicles.txt')

def check_path(path):
    """Checks if a path exists, and reads text if possible."""
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print("Sorry, this file does not exist!")
    else:
        print(contents)

check_path(path)