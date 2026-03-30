# A scouting report tool needs to load a data file stored in a
# subfolder called reports/ inside your current working directory.
# The file is called week1.txt and contains scouting notes.
#
# Your job: read and print the contents of that file.

from pathlib import Path

path = Path('practice/week06_PCC_chapter10_practice/reports/week1.txt')
contents = path.read_text()
print(contents)