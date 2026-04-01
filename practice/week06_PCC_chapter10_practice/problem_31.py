# A property management company needs to store a tenant's lease
# details so they persist between program runs.
#
# Your job: save this dictionary to a file called lease.json.
#
# lease = {
#     'tenant': 'Sarah',
#     'unit': '4B',
#     'monthly_rent': 1850,
#     'lease_term': 12
# }

from pathlib import Path
import json

lease = {
    'tenant':'Sarah',
    'unit':'4B',
    'monthly_rent':1850,
    'lease_term':12
}

path_0 = Path('lease.json')
contents = json.dumps(lease)
path_0.write_text(contents)