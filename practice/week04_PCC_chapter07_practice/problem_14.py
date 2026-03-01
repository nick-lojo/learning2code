# You're building an access control tool for a gym.
#
# Ask the user for their age.
# If they are 16 or older, print that they are eligible for a membership.
# If they are under 16, print that they are not eligible.

prompt = "What is your age? "
age = input(prompt)
age = int(age)

if age >= 16:
    print("You are old enough for a gym membership.")
else:
    print("Sorry, you must be 16 or older to qualify for a gym membership.")