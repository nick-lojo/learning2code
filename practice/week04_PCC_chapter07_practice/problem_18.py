# You're building a note-taking tool for a legal assistant.
#
# Continuously ask the user to enter a case note.
# The tool should stop when the user is finished.
# Print each note back as confirmation.

# I am using an active flag for this since the instructions say continuous.
# I do not think != makes sense here.

active = True
message = ""

while active:
    message = input("Enter your case note. When you are done, enter 'quit'. ")
    if message == 'quit':
        active = False
    else:
        print(f'Note Confirmation: "{message}"')