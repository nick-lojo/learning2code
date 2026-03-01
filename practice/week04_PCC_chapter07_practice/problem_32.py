# You're building a prompt for a customer feedback kiosk at an airport.
#
# The kiosk should first explain to the traveler why their feedback matters,
# then ask for their input on a new line.
# Print their response as confirmation.

prompt = "We truly value input from our customers."
prompt += "\nIt helps us improve airport operations."
prompt += "\nCould you please provide feedback on your experience here? "

feedback = input(prompt)
print(f'Submission Confirmation: "{feedback}"')