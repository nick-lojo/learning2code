# A race steward tool needs to log a single official ruling to
# a file called ruling.txt. The ruling is a single line of text.
#
# Your job: write the ruling to the file and confirm it worked
# by opening ruling.txt after running your script.
#
# Ruling: "Car 44 penalized 5 seconds for track limits violation."

from pathlib import Path

path = Path('ruling.txt')
contents = 'Ruling: "Car 44 penalized 5 seconds for track limits violation."'
path.write_text(contents)