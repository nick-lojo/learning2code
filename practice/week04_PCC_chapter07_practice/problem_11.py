# You're processing a waitlist for a restaurant reservation system.
#
# Start with a list of waiting guests and an empty list for seated guests.
# Move each guest from the waitlist to the seated list one at a time.
# Print a message as each guest is seated.
# After all guests are seated, print the full seated list.
#
# Waitlist: ['garcia', 'chen', 'patel', 'okonkwo']

waitlist = ['garcia', 'chen', 'patel', 'okonkwo']
seated = []

while waitlist:
    seated_guest = waitlist.pop()
    print(f"{seated_guest.title()} has been seated.")
    seated.append(seated_guest)

print("\nSeated Guests:")
for guest in seated:
    print(f"{guest.title()}")