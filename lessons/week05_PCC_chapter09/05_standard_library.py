# Chapter 9 Part 5: The Python Standard Library (PCC, pg. 179-181)

# randint returns a random integer between two vales, inclusive

from random import randint
print(randint(1, 6))

# choice returns a randomly selected element from a list or tuple

from random import choice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
first_up = choice(players)
print(first_up)

# 9-13. Dice: Make a class Die with one attribute called sides,
# which has a default value of 6. Write a method called
# roll_die() that prints a random number between 1 and the
# number of sides the die has. Make a 6-sided die and roll
# it 10 times.
# Make a 10-sided die and a 20-sided die. Roll each die 10 times.

from random import randint

class Dice:
    """A simple class used to model the behavior of a diee."""
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        """A method that simulates the roll of a die."""
        print(f"The {self.sides}-sided die rolled a {randint(1, self.sides)}")
    
    def ten_rolls(self):
        """Rolls a die ten times."""
        times_rolled = 1
        while times_rolled <= 10:
            self.roll_die()
            times_rolled += 1

standard_die = Dice()
standard_die.roll_die()
print("\n")
standard_die.ten_rolls()
print("\n")

ten_sided = Dice(sides=10)
ten_sided.roll_die()
print("\n")
ten_sided.ten_rolls()
print("\n")

twenty_sided = Dice(sides=20)
twenty_sided.roll_die()
print("\n")
twenty_sided.ten_rolls()

# 9-14. Lottery: Make a list or tuple containing a series of
# 10 numbers and 5 letters. Randomly select 4 numbers or
# letters from the list and print a message saying that any
# ticket matching these 4 numbers or letters wins a prize.

from random import choice

def select_winner(available, picked):
    """A function that selects the winner of a lottery."""
    inputs_selected = 1

    while inputs_selected <= 4:
        selected = choice(available)
        picked.append(selected)
        inputs_selected += 1

    print(f"The winning combo is {picked}. Any ticket matching this combo wins!")

ticket_inputs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c', 'd', 'e']
winning_combo = []

select_winner(ticket_inputs, winning_combo)

# 9-15. Lottery Analysis: You can use a loop to see how hard
# it might be to win the kind of lottery you just modeled.
# Make a list or tuple called my_ticket. Write a loop that
# keeps pulling numbers until your ticket wins. Print a
# message reporting how many times the loop had to run to
# give you a winning ticket.

my_ticket = [2, 4, 8, 7]

def lottery_analysis(available, ticket):
    """Runs lottery until winning combo matches ticket."""
    winning_combo = []
    loops_ran = 0

    while winning_combo != ticket:
        winning_combo = []
        select_winner(available, winning_combo)
        loops_ran += 1

    print(f"It took {loops_ran} tries to pull ypur ticket!")

lottery_analysis(ticket_inputs, my_ticket)