# You're building a sign-up tool for a conference registration system.
#
# Continuously ask each attendee for their name and their session preference.
# Store each response in a dictionary, with the attendee's name as the key.
# After each entry, ask if there are more attendees to register.
# If the user enters 'no', stop collecting responses.
# Print all registrations when done.

responses = {}
polling_active = True

while polling_active:
    name = input("What is your name? ")
    response = input("What is your session preference? ")

    responses[name] = response

    repeat = input("Does anyone else need to indicate their preference?"
    "(yes / no) ")
    if repeat == 'no':
        polling_active = False

print("\n––Results––")
for name, response in responses.items():
    print(f"{name.title()} would like to attend the {response.title()} Session.")