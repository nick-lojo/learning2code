# You're building a message intake tool for a customer support line.
#
# Continuously ask the user to enter a support message.
# Keep repeating until the user types 'quit'.
# Print each message back to the user as confirmation, but do not print 'quit'.

prompt = "Please enter your support message."
prompt += "\nPlease enter 'quit' once you have entered your support message. "

message = ""

while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(f'Message confirmation: "{message}"')