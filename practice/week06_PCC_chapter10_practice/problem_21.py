# A restaurant app saves a customer's favorite order to disk
# so it can be retrieved on their next visit.
#
# Your job: save this dictionary to a file called order.json,
# then read it back and print it.
#

from pathlib import Path
import json

order = {'name': 'Nick', 'item': 'burger', 'size': 'large'}
path = Path('order.json')
contents = json.dumps(order)
path.write_text(contents)