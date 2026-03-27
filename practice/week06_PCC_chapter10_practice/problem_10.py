# A sports analytics tool needs to count the total number of
# words in a post-game report. The report is stored in a file
# called report.txt.
#
# Your job: read the file, count the words, and print the result.
# Handle the case where the file doesn't exist.

from pathlib import Path

path = Path('report.txt')
contents = path.read_text()

print(f"The file {path} is {len(contents.split())} words long.")