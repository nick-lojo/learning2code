# A coaching app needs to save a list of play numbers to disk
# so they can be retrieved later. The list should survive after
# the program stops running.
#
# Your job: store this list in a file called plays.json.
# plays = [22, 34, 15, 7, 41]

plays = [22, 34, 15, 7, 41]

from pathlib import Path
import json

path = Path('plays.json')
contents = json.dumps(plays)
path.write_text(contents)