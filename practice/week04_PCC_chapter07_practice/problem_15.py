# You're building a feedback collector for a food delivery app.
#
# Continuously ask the user to enter a complaint or comment.
# Keep running until the user types 'quit'.
# Print each entry back as confirmation.
# Do not print 'quit'.

active = True
message = ""

while active:
    message = input("Please provide your feedback: ")
    if message == 'quit':
        active = False
    else:
        print(f'Response Confirmed: "{message}"')