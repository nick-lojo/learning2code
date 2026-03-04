# You're building a coffee order tool for an office kitchen app.
#
# Write a tool that accepts a drink type, but defaults to 'coffee' if
# nothing is specified.
# Place one order using the default, and one order specifying 'tea'.

def order_coffee(name, drink='coffee'):
    """A tool for office workers to place their drink order from a coffee shop."""
    print("\nOrder Details")
    print(f"\tName: {name.title()}")
    print(f"\tDrink: {drink}")

order_coffee('derek')
order_coffee('george', drink='tea')