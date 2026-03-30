# A recipe app saved ingredients to a file called ingredients.json
# in a previous session. A new script needs to load that data back
# into memory and print the list.

from pathlib import Path
import json

path = Path('ingredients.json')
contents = path.read_text()
ingredients = json.loads(contents)
print(ingredients)