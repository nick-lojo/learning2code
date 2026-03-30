# An inventory system stores product data in a file called
# stock.json that was saved in a previous session.
# A new script needs to load that data and print each item.

from pathlib import Path
import json

path = Path('stock.json')
contents = path.read_text(encoding='utf-8')
stock = json.loads(contents)
print(stock)