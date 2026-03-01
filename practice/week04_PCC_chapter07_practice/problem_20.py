# You're building a monitoring tool for a server admin.
#
# Each cycle, ask the admin for a status update.
# The session can end for multiple reasons.
# Print an appropriate message when the session ends.

active = True
message = ""

while active:
    message = input("Status Update: ")
    if message == 'inactive':
        active = False
    elif message == 'quit':
        active = False
    else:
        print("Session is still active, please continue.")
    if active == False:
        print("\nSession ended by admin.")