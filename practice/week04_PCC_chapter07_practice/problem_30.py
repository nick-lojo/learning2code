# You're building a filtering tool for an event ticketing platform.
#
# Continuously ask the user to enter a section they want to sit in.
# Only print seat assignments for even-numbered sections.
# Odd-numbered sections should be skipped silently.
# The tool should stop when the user is finished.

active = True

while active:
    message = input("Which section would you like to sit in? Enter 'quit' when done. ")
    if message == 'quit':
        active = False
        print("Thank you for choosing your seats!")
    else:
        message = int(message)
        if message % 2 == 0:
            print(f"Seat Assignment: Section {message}")
        else:
            continue