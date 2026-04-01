# A travel app saved a user's trip preferences to a file called
# preferences.json in a previous session. A new script needs to
# load that data and print each preference.

from pathlib import Path
import json

path_0 = Path('preferences.json')
contents = path_0.read_text()
preferences = json.loads(contents)

for preference, user_data in preferences.items():
    print(f"{preference.title()}: {user_data}")