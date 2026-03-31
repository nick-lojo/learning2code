# The coaching app from before saved a list of play numbers to
# plays.json. A new script needs to load that data back into
# memory and print the list.
#
# Your job: read plays.json and recover the original list.

from pathlib import Path
import json

path = Path('plays.json')
contents = path.read_text()
plays = json.loads(contents)
print(plays)