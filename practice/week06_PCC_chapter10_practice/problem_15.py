# A fantasy sports app prompts a user for their team name the
# first time they run it. On subsequent runs, it should greet
# them by their saved team name without asking again.
#
# Your job: save the team name to a file if it doesn't exist.
# Load and display it if it does.

from pathlib import Path
import json

def fantasy_team(path):
    """Either welcomes a player back using their team name, or prompts them
    to create one."""
    if path.exists():
        contents = path.read_text()
        team_name = json.loads(contents)
        print(f"\nWelcome back, {team_name.title()}!")
    else:
        print("\nIt looks like we cannot find your team in our database.")
        print("Please start by naming your team.")

        team_name = input("\nWhat would you like to name your team? ")
        contents = json.dumps(team_name)
        path.write_text(contents)
        print(f"We will remember you when you return, {team_name.title()}!")

path_0 = Path('teams.json')
fantasy_team(path_0)