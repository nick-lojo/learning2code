# A board game app needs to simulate dice rolls and randomly
# select which player goes first from a list of participants.
#
# Build both mechanics and demonstrate them.

from random import randint
from random import choice

class Dice:
    """Builds a die, including number of sides."""
    def __init__(self, sides):
        """Defines attributes of the die."""
        self.sides = sides

    def roll_die(self, player):
        """A method that rolls the die."""
        print(f"{player} rolled a {randint(1, self.sides)}!")

def pick_player(players):
    """A function that picks from the list of players to decide who goes first."""
    player_1 = choice(players)
    print(f"{player_1.title()} rolls first!")
    return player_1.title()

game_players = ['jane', 'john', 'louise', 'marty', 'barb', 'larry']
standard_die = Dice(6)

first_player = pick_player(game_players)
standard_die.roll_die(first_player)