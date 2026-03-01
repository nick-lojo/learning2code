# You're building an age verification tool for an online platform.
#
# Ask the user for their age and determine if they are old enough to access
# the site.
# The minimum age requirement is 18.
# Print an appropriate message based on their age.

prompt = "Please verify your age before entering the website: "

response = input(prompt)

response = int(response)

if response >= 18:
    print("You are old enough to enter the site, proceed.")
else:
    print("Access Denied. You must be 18 to enter this site.")