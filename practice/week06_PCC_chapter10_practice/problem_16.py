# The fantasy sports app is getting messy. The login logic,
# the file handling, and the greeting are all tangled together
# in one function.
#
# Your job: break the existing code into smaller functions,
# each with a single clear purpose. The program should behave
# exactly the same as before.

from pathlib import Path
import json

def create_team(path):
    """A function used for first-time users to save their team name."""
    print("\nWelcome to our app! Let's start by saving your team name.")

    team_name = input("\nWhat would you like to name your team? ")
    contents = json.dumps(team_name)
    path.write_text(contents)
    print(f"\nWe will remember you when you return, {team_name.title()}!")

def welcome_back(path):
    """Greets returning users."""
    contents = path.read_text()
    team_name = json.loads(contents)
    print(f"\nWelcome back, {team_name.title()}!")

def load_app(path):
    """Starts the app according to the users past-use."""
    if path.exists():
        welcome_back(path)
    else:
        create_team(path)

path_0 = Path('fantasy_teams.json')
load_app(path_0)