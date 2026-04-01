# A fitness app asks a new user for their name and goal weight
# on first run. On subsequent runs, it greets them by name and
# reminds them of their goal. The data should persist between
# runs.
#
# Your job: build this so it works correctly on both first run
# and return visits.

from pathlib import Path
import json

def new_user(path):
    """Collects data from new users, and stores them in a json file."""
    message = "\nWelcome to our app! Let's start by collecting some important"
    message += " information about you and your goals."
    print(message)

    name = input("\nWhat is your name? ")
    goal_weight = input("What is your goal weight (in lbs)? ")
    print("\nYou are now registered! We will remember this when you come back!")
    
    user_info = {
        'name':name,
        'goal weight':goal_weight
    }
    contents = json.dumps(user_info)
    path.write_text(contents)

def returning_user(path):
    """Greets returning users when they open the app."""
    contents = path.read_text()
    user_info = json.loads(contents)
    
    message = f"\nWelcome back, {user_info['name'].title()}! Let's work towards"
    message += f" that goal weight of {user_info['goal weight']} lbs!"
    print(message)

def launch_app(path):
    """Launches the app based on if a user is new or returning."""
    if path.exists():
        returning_user(path)
    else:
        new_user(path)

path_0 = Path('user_info.json')
launch_app(path_0)