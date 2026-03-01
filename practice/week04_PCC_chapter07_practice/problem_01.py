# You're building a check-in tool for a clinic's front desk.
#
# Ask the patient for their name, then print a personalized greeting.

prompt = "Please state your name. "

message = input(prompt)

print(f"Welcome to our practice, {message.title()}!")