# A ticket sales system stores daily sales reports in a subfolder
# called reports/ inside your current working directory.
# The file is called daily_sales.txt.
#
# Your job: read and print the contents of that file.

from pathlib import Path

path = Path('reports/daily_sales.txt')
contents = path.read_text()
print(contents)