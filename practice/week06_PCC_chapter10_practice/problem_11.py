# A word count tool needs to analyze multiple game reports at
# once. Each file may or may not exist.
#
# Your job: write a function that counts words in a single file
# and handles missing files. Then call that function on each
# of these files: report.txt, notes.txt, summary.txt.

from pathlib import Path

path_0 = Path('report.txt')
path_1 = Path('notes.txt')
path_2 = Path('summary.txt')

files = [path_0, path_1, path_2]

def count_words(list):
    """Counts the words in a file while omitting errors."""
    for file in list:
        try:
            content = file.read_text()
        except FileNotFoundError:
            print(f"Sorry, {file} does not exist.")
        else:
            print(f"There are {len(content.split())} words in {file}.")

count_words(files)