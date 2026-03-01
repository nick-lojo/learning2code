# You're building a tool for a parking enforcement officer.
#
# Ask the officer to enter a license plate number for each vehicle they flag.
# The tool should stop when the officer is done.
# Print each plate back as confirmation.

prompt = "Please enter the license plate for the illegally parked car."
prompt += "\nWhen you are done, enter 'quit'. "
message = ""

while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(f"Ticket issued for license plate {message}.")