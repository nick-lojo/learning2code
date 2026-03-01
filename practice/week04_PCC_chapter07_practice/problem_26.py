# You're building a toll booth calculator for a highway system.
#
# Ask the driver for their vehicle class number.
# Even-numbered classes use the express lane.
# Odd-numbered classes use the standard lane.
# Print the appropriate lane assignment.

prompt = "What is your vehicle's class number? "
class_number = input(prompt)
class_number = int(class_number)

if class_number % 2 == 0:
    print("Please proceed to the express lane.")
else:
    print("Please proceed to the standard lane.")