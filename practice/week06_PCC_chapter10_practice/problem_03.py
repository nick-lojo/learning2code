# A teammate stored a data file in a subfolder called race_data/
# inside your current working directory.
# The file is called results.txt and contains:
#   Lap 1: 32.4
#   Lap 2: 31.8
#
# Your job: read and print the contents of that file without
# moving it or changing your working directory.

from pathlib import Path
path = Path('race_data/results.txt')
contents = path.read_text()
print(contents)