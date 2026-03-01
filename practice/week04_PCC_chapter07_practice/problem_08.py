# You're building a city search tool for a travel app.
#
# Continuously ask the user to enter a city they want to explore.
# When the user types 'quit', exit immediately without printing anything
# further.
# For each valid city entered, print a confirmation message.

active = True
message = ""
prompt = "Name a city you would like to explore:"
prompt += "\nWhen you are done, enter 'quit'. "

while active:
    message = input(prompt)
    if message == 'quit':
        break
    else:
        print(f"{message.title()} would be a wonderful place to visit!")