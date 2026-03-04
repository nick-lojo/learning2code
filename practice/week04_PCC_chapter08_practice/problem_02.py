# You're building a client greeting tool for a wealth management firm.
#
# Write a tool that accepts a client's name and prints a personalized welcome.
# Greet three different clients.

def greeting(name):
    """Tool that greets clients at a wealth management firm."""
    print(f"Welcome, {name.title()}, to our firm!")

greeting('mary')
greeting('john')
greeting('melody')