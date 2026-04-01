# A logistics company stores shipment records in a file called
# shipments.txt. A tool needs to count the total number of words
# across the entire file and report the count.
#
# Your job: read the file, count the words, and print the result.

from pathlib import Path

def count_words(path):
    """Counts the total number of words in a file."""
    contents = path.read_text()
    words = contents.split()
    print(f"\nThere are {len(words)} words in the file {path}.")

path_0 = Path('shipments.txt')
count_words(path_0)