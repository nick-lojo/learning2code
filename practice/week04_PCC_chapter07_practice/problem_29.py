# You're building a quality control tool for a manufacturing line.
#
# Each cycle, ask the inspector for a status update on the line.
# The line can be shut down for multiple reasons.
# Print an appropriate message when the line is shut down.

active = True
message = ""

while active:
    message = input("Please provide a status update: ")
    if message == 'emergency':
        active = False
    elif message == 'malfunction':
        active = False
    elif message == 'manual shutdown':
        active = False
    else:
        print("The line is still active.")
    if active == False:
        print("The line has been shut down.")