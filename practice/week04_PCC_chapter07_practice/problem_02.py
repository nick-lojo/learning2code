# You're collecting feedback for a customer survey.
#
# Build a two-line prompt that first explains the purpose of the survey,
# then asks the customer for their response on a new line.
# Print their response back to them as confirmation.

prompt = "We are collecting feedback from customers."
prompt += "\nIn a few words, can you tell us if you are satisfied with your experience? "

response = input(prompt)

print(f'To confirm, you wrote: "{response}".')