# You're writing a tool for a parking garage attendant.
#
# Ask the user to enter a parking spot number.
# If the spot number is even, print that it is on the left side of the garage.
# If the spot number is odd, print that it is on the right side of the garage.

prompt = "Please enter your spot number: "

response = input(prompt)

response = int(response)

if response % 2 == 0:
    print(f"Spot #{response} is on the left side of the garage.")
else:
    print(f"Spot #{response} is on the right side of the garage.")