# You're creating a directory listing.
#
# You have a files dictionary with file sizes:
# - report.pdf: 2500
# - data.csv: 1800
# - image.png: 3200
# - notes.txt: 450
#
# Print each filename in alphabetical order, one per line.
# Don't print the file sizes.

files = {
    'report.pdf':2500,
    'data.csv':1800,
    'image.png':3200,
    'notes.txt':450
}

for key in sorted(files.keys()):
    print(key)