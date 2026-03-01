# You're building a search tool for a library catalog.
#
# Continuously ask the user to enter a book title to search.
# The tool should stop when the user is finished.
# Print each title back as confirmation.

prompt = "Enter the book title you would like to search for."
prompt += "\nWhen you are done, enter 'quit. "
message = ""

while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(f'Searching for "{message.title()}"')